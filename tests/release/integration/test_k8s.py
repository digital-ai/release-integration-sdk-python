from types import SimpleNamespace
from unittest import mock

import pytest
from kubernetes.config.config_exception import ConfigException

from digitalai.release.integration import k8s


def test_split_secret_resource_data_returns_namespace_name_and_key():
    assert k8s.split_secret_resource_data("runner-ns:result-secret:result") == ("runner-ns", "result-secret", "result")


@pytest.mark.parametrize("entry", ["", None])
def test_split_secret_resource_data_rejects_an_empty_reference(entry):
    with pytest.raises(ValueError, match="empty"):
        k8s.split_secret_resource_data(entry)


@pytest.mark.parametrize("entry", ["name", "ns:name", "ns:name:key:extra"])
def test_split_secret_resource_data_rejects_a_malformed_reference(entry):
    with pytest.raises(ValueError, match="namespace:name:key"):
        k8s.split_secret_resource_data(entry)


@pytest.fixture
def kube(monkeypatch):
    """Stands in for the kubernetes config loaders and client classes, with no cached client."""
    fake = SimpleNamespace(config=mock.Mock(), client=mock.Mock())
    fake.client.Configuration.get_default_copy.return_value = SimpleNamespace(verify_ssl=True)
    monkeypatch.setattr(k8s, "config", fake.config)
    monkeypatch.setattr(k8s, "client", fake.client)
    monkeypatch.setattr(k8s, "kubernetes_client", None)
    monkeypatch.delenv("SKIP_TLS_LEGACY_K8S", raising=False)
    return fake


def test_get_client_uses_the_in_cluster_config(kube):
    client = k8s.get_client()

    kube.config.load_incluster_config.assert_called_once_with()
    kube.config.load_config.assert_not_called()
    assert client is kube.client.CoreV1Api.return_value


def test_get_client_falls_back_to_the_default_config_outside_a_cluster(kube):
    kube.config.load_incluster_config.side_effect = ConfigException("not in a pod")

    k8s.get_client()

    kube.config.load_config.assert_called_once_with()


def test_get_client_raises_when_no_config_can_be_loaded(kube):
    kube.config.load_incluster_config.side_effect = ConfigException("not in a pod")
    kube.config.load_config.side_effect = ConfigException("no kubeconfig")

    with pytest.raises(RuntimeError, match="Could not configure Kubernetes client"):
        k8s.get_client()


def test_get_client_creates_the_client_once(kube):
    first = k8s.get_client()
    second = k8s.get_client()

    assert first is second
    kube.config.load_incluster_config.assert_called_once()
    kube.client.CoreV1Api.assert_called_once()


@pytest.mark.parametrize("value", ["true", "TRUE"])
def test_get_client_disables_tls_verification_for_legacy_clusters(kube, monkeypatch, value):
    monkeypatch.setenv("SKIP_TLS_LEGACY_K8S", value)

    k8s.get_client()

    (configuration,), _ = kube.client.ApiClient.call_args
    assert configuration.verify_ssl is False
    kube.client.CoreV1Api.assert_called_once_with(kube.client.ApiClient.return_value)


@pytest.mark.parametrize("value", [None, "false", "yes"])
def test_get_client_keeps_tls_verification_otherwise(kube, monkeypatch, value):
    if value is not None:
        monkeypatch.setenv("SKIP_TLS_LEGACY_K8S", value)

    k8s.get_client()

    kube.client.ApiClient.assert_not_called()
    kube.client.CoreV1Api.assert_called_once_with()
