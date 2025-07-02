import dowhy

class CausalAnalyzer:
    def __init__(self):
        pass

    def identify_causal_effect(self, data, treatment, outcome):
        model = dowhy.CausalModel(
            data=data,
            treatment=treatment,
            outcome=outcome,
            common_causes="auto"
        )
        identified_estimand = model.identify_effect()
        estimate = model.estimate_effect(
            identified_estimand,
            method_name="backdoor.propensity_score_matching"
        )
        return estimate.value
