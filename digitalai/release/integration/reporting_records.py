from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from dataclasses_json import dataclass_json, LetterCase, config
from marshmallow import fields


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BuildRecord:
    """
     BuildRecord is a data model class which represents the record of a build.
    """
    target_id: str
    build: str
    build_url: str = field(metadata=config(field_name="build_url"))
    project: str
    outcome: str
    start_date: datetime = field(metadata=config(encoder=datetime.isoformat, decoder=datetime.fromisoformat,
                                                 mm_field=fields.DateTime(format='iso')))
    end_date: datetime = field(metadata=config(encoder=datetime.isoformat, decoder=datetime.fromisoformat,
                                               mm_field=fields.DateTime(format='iso')))
    duration: str
    type: str = "udm.BuildRecord"
    id: str = ""
    server_url: Optional[str] = None
    server_user: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlanRecord:
    """
     PlanRecord is a data model class which represents the record of a plan.
    """
    target_id: str
    ticket: str
    ticket_url: str = field(metadata=config(field_name="ticket_url"))
    title: str
    ticket_type: str
    status: str
    updated_date: datetime = field(metadata=config(encoder=datetime.isoformat, decoder=datetime.fromisoformat,
                                                   mm_field=fields.DateTime(format='iso')))
    type: str = "udm.PlanRecord"
    id: str = ""
    updated_by: Optional[str] = None
    server_url: Optional[str] = None
    server_user: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ItsmRecord:
    """
     ItsmRecord is a data model class which represents the record of IT Service Management.
    """
    target_id: str
    record: str
    record_url: str = field(metadata=config(field_name="record_url"))
    title: str
    status: str
    priority: str
    created_by: str
    type: str = "udm.ItsmRecord"
    id: str = ""
    server_url: Optional[str] = None
    server_user: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CodeComplianceRecord:
    """
     CodeComplianceRecord is a data model class which represents the record of a Security and Compliance.
    """
    target_id: str
    project: str
    project_url: str = field(metadata=config(field_name="project_url"))
    analysis_date: datetime = field(metadata=config(encoder=datetime.isoformat, decoder=datetime.fromisoformat,
                                                    mm_field=fields.DateTime(format='iso')))
    outcome: str
    compliance_data: str
    type: str = "udm.CodeComplianceRecord"
    id: str = ""
    server_url: Optional[str] = None
    server_user: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DeploymentRecord:
    """
     DeploymentRecord is a data model class which represents the record of a Deployment.
    """
    target_id: str
    deployment_task: str
    deployment_task_url: str = field(metadata=config(field_name="deploymentTask_url"))
    status: str
    version: str
    type: str = "udm.DeploymentRecord"
    id: str = ""
    application_name: Optional[str] = None
    environment_name: Optional[str] = None
    server_url: Optional[str] = None
    server_user: Optional[str] = None


def _decimal_string(value) -> Optional[str]:
    """Sends a cost as the decimal string the server stores, e.g. Decimal("0.0123") -> "0.0123"."""
    return None if value is None else str(value)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AiUsageRecord:
    """
     AiUsageRecord is a data model class which represents one AI agent execution attempt of a task:
     the language model provider and model, the agent, why it stopped, and its token usage and cost.

     The record's start and end times are taken from the task. The provider's endpoint and user go in
     server_url and server_user. estimated_cost is a decimal string; pass a str or a Decimal, since a
     float can carry rounding noise (str(0.1 + 0.2) is "0.30000000000000004").

     Only add it on a Release version that defines udm.AiUsageRecord: an older server cannot read
     the task's result and fails the task, without its output properties.
    """
    target_id: str
    llm_provider: Optional[str] = None
    agent: Optional[str] = None
    model: Optional[str] = None
    termination_reason: Optional[str] = None
    iterations: Optional[int] = None
    tool_calls: Optional[int] = None
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    total_tokens: Optional[int] = None
    estimated_cost: Optional[str] = field(default=None, metadata=config(encoder=_decimal_string))
    currency: str = "USD"
    type: str = "udm.AiUsageRecord"
    id: str = ""
    server_url: Optional[str] = None
    server_user: Optional[str] = None
