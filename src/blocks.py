def markdown_to_blocks(markdown):
    strings_block = markdown.split("\n\n")
    filtered_block = []
    for block in strings_block:
        if block == "":
            continue
        block = block.strip()
        filtered_block.append(block)

    return filtered_block

def block_to_block_type(markdown):
    lines = markdown.split("\n")
    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    if markdown.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    if markdown.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return "paragraph"
        return "unordered_list"
    if markdown.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    
    if markdown.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    
    return "paragraph"