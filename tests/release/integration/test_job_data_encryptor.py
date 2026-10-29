import base64
import os

import pytest
from Cryptodome.Cipher import AES

from digitalai.release.integration.job_data_encryptor import AESJobDataEncryptor, NoOpJobDataEncryptor


def new_key() -> str:
    """A base64-encoded 256-bit key, as the server provides it."""
    return base64.b64encode(os.urandom(32)).decode()


@pytest.fixture
def encryptor():
    return AESJobDataEncryptor(new_key())


@pytest.mark.parametrize("content", ['{"exitCode": 0}', "", "ünïcødé ✓"])
def test_aes_decrypt_returns_what_encrypt_was_given(encryptor, content):
    assert encryptor.decrypt(encryptor.encrypt(content)) == content


def test_aes_encrypt_uses_a_fresh_nonce_per_call(encryptor):
    assert encryptor.encrypt("same") != encryptor.encrypt("same")


def test_aes_decrypts_the_nonce_ciphertext_tag_layout_the_server_produces():
    key = os.urandom(32)
    nonce = os.urandom(16)
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    ciphertext, tag = cipher.encrypt_and_digest(b'{"task": {}}')
    payload = base64.b64encode(nonce + ciphertext + tag).decode()

    assert AESJobDataEncryptor(base64.b64encode(key).decode()).decrypt(payload) == '{"task": {}}'


def test_aes_decrypt_rejects_tampered_content(encryptor):
    raw = bytearray(base64.b64decode(encryptor.encrypt("payload")))
    raw[20] ^= 0xFF

    with pytest.raises(ValueError):
        encryptor.decrypt(base64.b64encode(bytes(raw)).decode())


def test_aes_decrypt_rejects_content_encrypted_with_another_key(encryptor):
    with pytest.raises(ValueError):
        AESJobDataEncryptor(new_key()).decrypt(encryptor.encrypt("payload"))


@pytest.mark.parametrize("method", ["encrypt", "decrypt"])
def test_noop_returns_content_unchanged(method):
    assert getattr(NoOpJobDataEncryptor(), method)('{"a": 1}') == '{"a": 1}'
