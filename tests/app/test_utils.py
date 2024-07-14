from nitka.app.utils import extract_table_names, FieldType


class TestExtractTableNames:
    def test_target_only(self, yml_data_target):
        assert extract_table_names(yml_data_target, FieldType.SOURCE) == set()
        assert extract_table_names(yml_data_target, FieldType.TARGET) == {"table_config_1"}

    def test_source_only(self, yml_data_source):
        assert extract_table_names(yml_data_source, FieldType.SOURCE) == {"table_config_1"}
        assert extract_table_names(yml_data_source, FieldType.TARGET) == set()

    def test_source_and_target(self, yml_data_source_target):
        assert extract_table_names(yml_data_source_target, FieldType.SOURCE) == {"table_1_config_1"}
        assert extract_table_names(yml_data_source_target, FieldType.TARGET) == {"table_2_config_1"}

    def test_no_source_no_target(self, yml_data_no_source_no_target):
        assert extract_table_names(yml_data_no_source_no_target, FieldType.SOURCE) == set()
        assert extract_table_names(yml_data_no_source_no_target, FieldType.TARGET) == set()

    def test_multiple_values(self, yml_data_multiple_values):
        assert extract_table_names(yml_data_multiple_values, FieldType.SOURCE) == {"table_1_config_1", "table_2_config_1"}
        assert extract_table_names(yml_data_multiple_values, FieldType.TARGET) == {"table_3_config_1", "table_4_config_1"}
