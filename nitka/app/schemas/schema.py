from pydantic import BaseModel


class Config(BaseModel):
    name: str
    service_config: dict | None
    source_tables: list[str] | None
    target_tables: list[str] | None

    class Config:
        from_attributes = True
