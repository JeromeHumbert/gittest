import re
s = '<study_first_posted type="Estimate">September 24, 1999</study_first_posted><last_update_submitted>September 16, 2009</last_update_submitted><last_update_submitted_qc>September 16, 2009</last_update_submitted_qc><last_update_posted type="Estimate">September 17, 2009</last_update_posted><condition_browse>'
s = re.sub('\<last_update_submitted.*?last_update_submitted>', '', s)
print(s)
