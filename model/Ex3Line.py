class Ex3Line:
    def __init__(self, state, state_name, state_fips, fema_region, overall_outcome, date, new_results_reported, total_results_reported):
        self.state = state
        self.state_name = state_name
        self.state_fips = state_fips
        self.fema_region = fema_region
        self.overall_outcome = overall_outcome
        self.date = date
        self.new_results_reported = new_results_reported
        self.total_results_reported = total_results_reported