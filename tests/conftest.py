import pytest
import yaml


@pytest.fixture
def yml_data_source_target_raw():
    return """
    job_step:
      step_name: step_1
      service_name: service_1
      service_config:
        transformation_step:
          source_database: refinery_prod
          source_table: table_1_config_1
          target_database: treasury_prod
          target_table: table_2_config_1
    """


@pytest.fixture
def yml_data_source_raw():
    return """
    job_step:
      step_name: step_1
      service_name: service_1
      service_config:
        transformation_step:
          source_database: refinery_prod
          source_table: table_config_1
    """


@pytest.fixture
def yml_data_target_raw():
    return """
    job_step:
      step_name: step_1
      service_name: service_1
      service_config:
        transformation_step:
          target_database: treasury_prod
          target_table: table_config_1
    """


@pytest.fixture
def yml_data_no_source_no_target_raw():
    return """
    job_step:
      step_name: step_1
      service_name: service_1
      service_config:
        landing_database: landing_prod
        landing_table: table_config_2
    """


@pytest.fixture
def yml_data_multiple_values_raw():
    return """
    job_step:
      step_name: step_1
      service_name: service_1
      service_config:
        transformation_step:
          landing_database: landing_prod
          landing_table: table_config_2
          source_tables: 
            - source_table: 
                table_name: table_1_config_1
            - source_table: 
                table_name: table_2_config_1
          target_tables: 
            - target_table: 
                table_name: table_4_config_1
            - target_table: 
                table_name: table_3_config_1
          source_database: refinery_prod
          target_database: treasury_prod
    """


@pytest.fixture
def yml_data_source_target(yml_data_source_target_raw):
    return yaml.safe_load(yml_data_source_target_raw)


@pytest.fixture
def yml_data_source(yml_data_source_raw):
    return yaml.safe_load(yml_data_source_raw)


@pytest.fixture
def yml_data_target(yml_data_target_raw):
    return yaml.safe_load(yml_data_target_raw)


@pytest.fixture
def yml_data_no_source_no_target(yml_data_no_source_no_target_raw):
    return yaml.safe_load(yml_data_no_source_no_target_raw)


@pytest.fixture
def yml_data_multiple_values(yml_data_multiple_values_raw):
    return yaml.safe_load(yml_data_multiple_values_raw)
