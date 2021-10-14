from openfisca_core.model_api import *
from openfisca_us.entities import *
from openfisca_us.tools.general import *

class StateGroup(Enum):
    CONTIGUOUS_US = "Contiguous US"
    AK = "Alaska"
    HI = "Hawaii"

class spm_unit_state_group(Variable):
    value_type = Enum
    possible_values = StateGroup
    default_value = StateGroup.CONTIGUOUS_US
    entity = SPMUnit
    label = u"State group"
    definition_period = ETERNITY


class poverty_ratio(Variable):
    value_type = float
    entity = SPMUnit
    label = u"poverty_ratio"
    definition_period = YEAR

    def formula(spm_unit, period):
        return spm_unit("SPM_unit_net_income", period) / spm_unit("poverty_threshold", period)


class children(Variable):
    value_type = int
    entity = SPMUnit
    label = u"children"
    definition_period = YEAR

    def formula(spm_unit, period):
        return spm_unit.sum(spm_unit.members("age", period) < 18)
