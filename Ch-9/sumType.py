from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


def convert_format(content, from_format, to_format):
    match (content, from_format, to_format):
        case (content, DocFormat.MD, DocFormat.HTML):
            return f"<h1>{content[2:]}</h1>"
            
        case (content, DocFormat.TXT, DocFormat.PDF):
            return f"[PDF] {content} [PDF]"
            
        case (content, DocFormat.HTML, DocFormat.MD):
            if content.startswith('<h1>') and content.endswith('</h1>'):
                return f"# {content[4:-5]}"
            else:
                raise Exception('Content is not a valid <h1> tag')
            
        case _:
            raise Exception('Invalid type')
