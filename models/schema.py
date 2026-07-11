from pydantic import BaseModel, ConfigDict, field_validator


class BriefResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    asset_type: str = ""
    number_of_assets: int = 0
    target_audience: str = ""
    core_message: str = ""
    deadline: str = ""
    priority: str = ""
    missing_information: str = ""
    recommended_next_step: str = ""
    status: str = ""
    duplicate: bool = False

    @field_validator("number_of_assets", mode="before")
    @classmethod
    def coerce_assets(cls, v: object) -> int:
        try:
            return int(v)
        except (TypeError, ValueError):
            return 0
