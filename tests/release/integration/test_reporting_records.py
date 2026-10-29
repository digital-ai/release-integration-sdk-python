"""
The serialized field names are the wire format the Release server reads, so
they are pinned here exactly, including the few that are not camelCase.
"""
import json
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from digitalai.release.integration import (
    AiUsageRecord,
    BuildRecord,
    CodeComplianceRecord,
    DeploymentRecord,
    ItsmRecord,
    OutputContext,
    PlanRecord,
)

WHEN = datetime(2026, 3, 4, 5, 6, 7, tzinfo=timezone.utc)
WHEN_ISO = "2026-03-04T05:06:07+00:00"

RECORDS = {
    "build": (
        BuildRecord(target_id="T1", build="#42", build_url="http://ci/42", project="app", outcome="SUCCESS",
                    start_date=WHEN, end_date=WHEN, duration="PT1M"),
        {"targetId": "T1", "build": "#42", "build_url": "http://ci/42", "project": "app", "outcome": "SUCCESS",
         "startDate": WHEN_ISO, "endDate": WHEN_ISO, "duration": "PT1M", "type": "udm.BuildRecord", "id": "",
         "serverUrl": None, "serverUser": None},
    ),
    "plan": (
        PlanRecord(target_id="T1", ticket="PRJ-1", ticket_url="http://jira/PRJ-1", title="Fix", ticket_type="Bug",
                   status="Done", updated_date=WHEN, updated_by="dev"),
        {"targetId": "T1", "ticket": "PRJ-1", "ticket_url": "http://jira/PRJ-1", "title": "Fix",
         "ticketType": "Bug", "status": "Done", "updatedDate": WHEN_ISO, "type": "udm.PlanRecord", "id": "",
         "updatedBy": "dev", "serverUrl": None, "serverUser": None},
    ),
    "itsm": (
        ItsmRecord(target_id="T1", record="CHG1", record_url="http://snow/CHG1", title="Change", status="New",
                   priority="P2", created_by="ops"),
        {"targetId": "T1", "record": "CHG1", "record_url": "http://snow/CHG1", "title": "Change", "status": "New",
         "priority": "P2", "createdBy": "ops", "type": "udm.ItsmRecord", "id": "", "serverUrl": None,
         "serverUser": None},
    ),
    "code-compliance": (
        CodeComplianceRecord(target_id="T1", project="app", project_url="http://sonar/app", analysis_date=WHEN,
                             outcome="PASSED", compliance_data="A"),
        {"targetId": "T1", "project": "app", "project_url": "http://sonar/app", "analysisDate": WHEN_ISO,
         "outcome": "PASSED", "complianceData": "A", "type": "udm.CodeComplianceRecord", "id": "",
         "serverUrl": None, "serverUser": None},
    ),
    "deployment": (
        DeploymentRecord(target_id="T1", deployment_task="Deploy", deployment_task_url="http://cd/1",
                         status="DONE", version="1.0", application_name="app", environment_name="prod"),
        {"targetId": "T1", "deploymentTask": "Deploy", "deploymentTask_url": "http://cd/1", "status": "DONE",
         "version": "1.0", "type": "udm.DeploymentRecord", "id": "", "applicationName": "app",
         "environmentName": "prod", "serverUrl": None, "serverUser": None},
    ),
    # Field names as udm.AiUsageRecord declares them in xl-release's AI reporting module.
    "ai-usage": (
        AiUsageRecord(target_id="T1", llm_provider="OpenAI", agent="Release agent", model="gpt-4o",
                      termination_reason="COMPLETED", iterations=3, tool_calls=5, input_tokens=1200,
                      output_tokens=300, total_tokens=1500, estimated_cost="0.0123", currency="EUR",
                      server_url="https://api.openai.com/v1", server_user="svc-release"),
        {"targetId": "T1", "llmProvider": "OpenAI", "agent": "Release agent", "model": "gpt-4o",
         "terminationReason": "COMPLETED", "iterations": 3, "toolCalls": 5, "inputTokens": 1200,
         "outputTokens": 300, "totalTokens": 1500, "estimatedCost": "0.0123", "currency": "EUR",
         "type": "udm.AiUsageRecord", "id": "", "serverUrl": "https://api.openai.com/v1",
         "serverUser": "svc-release"},
    ),
}


@pytest.mark.parametrize("record, expected", RECORDS.values(), ids=list(RECORDS))
def test_record_serializes_to_the_server_wire_format(record, expected):
    assert record.to_dict() == expected


@pytest.mark.parametrize("record, _", RECORDS.values(), ids=list(RECORDS))
def test_record_round_trips_through_its_dict_form(record, _):
    assert type(record).from_dict(record.to_dict()) == record


def test_output_context_serializes_camel_case_with_records_as_json():
    build, expected_build = RECORDS["build"]
    context = OutputContext(1, "failed", {"greeting": "Hello"}, [build, {"custom": 1}])

    assert json.loads(json.dumps(context.to_dict())) == {
        "exitCode": 1,
        "jobErrorMessage": "failed",
        "outputProperties": {"greeting": "Hello"},
        "reportingRecords": [expected_build, {"custom": 1}],
    }


def test_ai_usage_record_needs_only_the_task_and_defaults_the_currency_to_usd():
    assert AiUsageRecord(target_id="T1").to_dict() == {
        "targetId": "T1", "llmProvider": None, "agent": None, "model": None, "terminationReason": None,
        "iterations": None, "toolCalls": None, "inputTokens": None, "outputTokens": None, "totalTokens": None,
        "estimatedCost": None, "currency": "USD", "type": "udm.AiUsageRecord", "id": "", "serverUrl": None,
        "serverUser": None,
    }


def test_ai_usage_record_sends_a_decimal_cost_as_its_exact_decimal_string():
    record = AiUsageRecord(target_id="T1", estimated_cost=Decimal("0.000150"))

    assert json.loads(json.dumps(record.to_dict()))["estimatedCost"] == "0.000150"


def test_ai_usage_record_with_a_decimal_cost_serializes_inside_the_task_result():
    record = AiUsageRecord(target_id="T1", total_tokens=1500, estimated_cost=Decimal("0.0123"))

    (written,) = json.loads(json.dumps(OutputContext(0, "", {}, [record]).to_dict()))["reportingRecords"]

    assert (written["type"], written["totalTokens"], written["estimatedCost"]) == ("udm.AiUsageRecord", 1500, "0.0123")
