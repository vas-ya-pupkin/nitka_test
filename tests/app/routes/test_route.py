import pytest
from fastapi.testclient import TestClient

from nitka.app.main import app
from nitka.app import models
from nitka.app.models.database import SessionLocal

client = TestClient(app)


# TODO use a separate test database. The current approach works with the prod -> drops it


@pytest.fixture
def get_db():
    db = SessionLocal()
    db.query(models.Config).delete()
    db.commit()
    try:
        yield db
    finally:
        db.close()


class TestSave:
    def test_success(self, get_db: SessionLocal, yml_data_source_target_raw: str) -> None:
        payload = {"file": ("config.yml", yml_data_source_target_raw)}
        response = client.post("/config/", files=payload)
        assert response.status_code == 200
        assert response.json() == {
            "name": "service_1.step_1",
            "service_config": {
                "transformation_step": {
                    "source_database": "refinery_prod",
                    "source_table": "table_1_config_1",
                    "target_database": "treasury_prod",
                    "target_table": "table_2_config_1"
                }
            },
            "source_tables": ["table_1_config_1"],
            "target_tables": ["table_2_config_1"]
        }

    def test_exists(self, get_db: SessionLocal, yml_data_source_target_raw: str) -> None:
        payload = {"file": ("config.yml", yml_data_source_target_raw)}
        response = client.post("/config/", files=payload)
        assert response.status_code == 200
        response = client.post("/config/", files=payload)
        assert response.status_code == 400
        assert response.json() == {"detail": "Config already exists"}

    def test_invalid(self, get_db: SessionLocal) -> None:
        yaml_data = """definitely not a valid yaml file"""
        response = client.post("/config/", files={"file": ("config.yml", yaml_data)})
        assert response.status_code == 422
        assert response.json() == {"detail": "Invalid config file"}


class TestGet:
    def test_exists(self, get_db: SessionLocal, yml_data_multiple_values_raw: str) -> None:
        payload = {"file": ("config.yml", yml_data_multiple_values_raw)}
        client.post("/config/", files=payload)

        response = client.get("/config/?name=service_1.step_1")
        assert response.status_code == 200
        assert response.json() == {
            "name": "service_1.step_1",
            "service_config": {
                "transformation_step": {
                    "landing_database": "landing_prod",
                    "landing_table": "table_config_2",
                    "source_database": "refinery_prod",
                    "source_tables": [
                        {"source_table": {"table_name": "table_1_config_1"}},
                        {"source_table": {"table_name": "table_2_config_1"}},
                    ],
                    "target_database": "treasury_prod",
                    "target_tables": [
                        {"target_table": {"table_name": "table_4_config_1"}},
                        {"target_table": {"table_name": "table_3_config_1"}},
                    ]
                }
            },
            "source_tables": ["table_1_config_1", "table_2_config_1"],
            "target_tables": ["table_4_config_1", "table_3_config_1"],
        }

    def test_not_found(self, get_db: SessionLocal) -> None:
        response = client.get("/config/?name=service_1.step_1")
        assert response.status_code == 404
        assert response.json() == {"detail": "Config not found"}

