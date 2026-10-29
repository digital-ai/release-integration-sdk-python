"""
The serialized field names are the wire format the Release server reads, so
they are pinned here exactly, including the few that are not camelCase.
"""
import json
from datetime import datetime, timezone

import pytest

from digitalai.release.integration import (
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
