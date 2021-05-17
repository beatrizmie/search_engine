import re


def limpa_url(texto):
    # Regex obtida de https://www.geeksforgeeks.org/python-check-url-string/
    pattern = r"""
        (?i)  # Ignore case.
        \b  # Inicio de palavra.
        (?:
            https?://
        |
            www
            \d{0,3}
            [.]
        |
            [a-z0-9.\-]+
            [.]
            [a-z]{2,4}
            /
        )
        (?:
            [^\s()<>]+
        |
            \(
            (?:
                [^\s()<>]+
            |
                \(
                [^\s()<>]+
                \)
            )*
            \)
        )+
        (?:
            \(
            (?:
                [^\s()<>]+
            |
                \(
                [^\s()<>]+
                \)
            )*
            \)
        |
            [^\s`!()\[\]{};:'\".,<>?«»“”‘’]
        )
    """
    repl = ''
    matcher = re.compile(pattern, re.VERBOSE)
    return matcher.sub(repl, texto)


def limpa_hashtags(texto):
    pattern = r"#\w+"
    repl = r" "
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def limpa_arroba(texto):
    pattern = r"@\w+"
    repl = r" "
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def limpa_aspas(texto):
    pattern = r"""['"“]+"""
    repl = r" "
    matcher = re.compile(pattern, re.VERBOSE)
    return matcher.sub(repl, texto)


def limpa_parenteses(texto):
    pattern = r"\(|\)"
    repl = r" "
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def limpa_pontuacoes(texto):
    pattern = r"[!@#$%^&*<>,./?;:_-]+"
    repl = r" "
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def clean_text(texto):

    texto = limpa_url(texto)
    texto = limpa_arroba(texto)
    texto = limpa_hashtags(texto)
    texto = limpa_aspas(texto)
    texto = limpa_parenteses(texto)
    texto = limpa_pontuacoes(texto)
    texto = texto.lower()

    return texto
