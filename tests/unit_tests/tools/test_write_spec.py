from unittest.mock import Mock

import pytest

from superagi.tools.code.write_spec import WriteSpecTool


class MockBaseLlm:
    def chat_completion(self, messages, max_tokens):
        return {"content": "Generated specification"}

class TestWriteSpecTool:

    @pytest.fixture
    def tool(self):
        tool = WriteSpecTool()
        tool.llm = MockBaseLlm()
        tool.resource_manager = Mock()
        return tool

    def test_execute(self, tool):
        tool.resource_manager.write_file = Mock()
        tool.resource_manager.write_file.return_value = "File write successful"
        response = tool._execute("Test task description", "test_spec_file.txt")
        assert response == "Generated specificationSpecification generated and saved successfully"
        tool.resource_manager.write_file.assert_called_once_with("test_spec_file.txt", "Generated specification")
