from llama_index.legacy.prompts import PromptTemplate


def get_prompt_template():
    instructions = """\
        1. Convert the query to executable Python code using Pandas.
        2. The final line of code should be a Python expression that can be called with the `eval()` function.
        3. The code should represent a solution to the query.
        4. Print only the expression.
        5. Do not quote the expression.
        6. Do not include any comments in the code.
    """
    prompt_template = PromptTemplate(
        """\
        You are working with a pandas dataframe in Python.
        The name of the dataframe is `df`.
        This is the result of `print(df.head())`:
        {df_str}

        Follow these instructions:
        {instructions}
        Query: {query_str}

        Expression:
        """
    )
    return instructions, prompt_template


def get_context():
    context = """
        Purpose: The primary role of this agent is to assist users by providing accurate
        information about world population statistics and details about a country.
    """
    return context
