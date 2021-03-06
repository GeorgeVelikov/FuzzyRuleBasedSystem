from models.term import Term;

class Rule:
    def __str__(self):
        value = "Rule: " + self.Name + "\n"

        activelyOpenParentheses = int();

        for term in self.Terms:
            currentTermClosingParentheses = term.ClosingParenthesesCount - term.OpeningParenthesesCount;
            activelyOpenParentheses -= currentTermClosingParentheses;

            value += str(term) + "\n" + (activelyOpenParentheses * "\t");

        value += str(self.Result);

        return value;

    def __init__(self, name, terms, result):
        self.Name = str();
        self.Terms = list();
        self.Result = Term;

        self.Name = name;
        self.Terms = terms;
        self.Result = result;

        return;

    def RaiseExceptionIfInvalid(self):
        # add necessary data checks here
        return True;