from langchain.tools import StructuredTool
from pydantic import BaseModel

def write_report(file, html):
    with open(file, 'w') as f:
        f.write(html)

class WriteReportArgsSchema(BaseModel):
    file:str
    html: str

# structured tool is used when you need to provide multiple arguments
write_report_tool = StructuredTool.from_function(
    name="write_report",
    description="Write an HTML file to disk. Use this tool whenever someone asks for a report.",
    func=write_report,
    args_schema=WriteReportArgsSchema
)