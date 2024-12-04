import InfoExtractor as infoex

# symptoms dictionary
symptom_priority = {
"Severe chest or abdominal pain": (4, "icu", "Hospital"),
"Difficulty breathing or shortness of breath": (4, "icu", "Hospital"),
"Uncontrollable bleeding": (4, "icu", "Hospital"),
"Sudden or severe injury": (4, "tc", "Hospital"),
"Head injury with loss of consciousness or confusion": (4, "tc", "Hospital"),
"Signs of a stroke": (4, "ccu", "Hospital"),
"Severe or persistent vomiting or diarrhea": (4, "icu", "Hospital"),
"Poisoning or suspected overdose": (4, "icu", "Hospital"),
"High fever or fever with a rash": (4, "icu", "Hospital"),
"Seizures or convulsions": (4, "icu", "Hospital"),
"Sudden collapse or unexplained fall": (3, "tc", "Hospital"),
"Sudden onset of weakness, numbness or paralysis": (3, "vc", "Hospital"),
"Suspected severe allergic reaction/ anaphylaxis": (3, "icu", "Hospital"),
"Suspected spinal injury": (3, "tc", "Hospital"),
"Unconsciousness": (3, "icu", "Hospital"),
"Any sudden, severe pain": (2, "icu", "Hospital"),
"Anything impaled in any part of the body": (2, "tc", "Hospital"),
"Broken bones or dislocated joints": (2, "tc", "Hospital"),
"Burns to face or genitals": (2, "tc", "Hospital"),
"Cuts with exposed tissue": (2, "tc", "Hospital"),
"Deep cuts": (2, "tc", "Hospital"),
"Embedded object in the eye": (2, "tc", "Hospital"),
"Flu-like symptoms that are severe or coughing up blood": (2, "icu", "Hospital"),
"Head injuries": (2, "tc", "Hospital"),
"Inability to urinate": (2, "icu", "Hospital"),
"Pain in pregnancy": (2, "icu", "Hospital"),
"Persistent high fever despite medication": (2, "icu", "Hospital"),
"Pregnancy - reduced movement": (2, "icu", "Hospital"),
"Pregnancy - ruptured membranes": (2, "icu", "Hospital"),
"Severe testicular pain": (2, "icu", "Hospital"),
"Sudden change in mental state or difficulty speaking": (2, "icu", "Hospital"),
"Sudden changes in vision": (2, "icu", "Hospital"),
"Unusual headaches or migraines": (2, "icu", "Hospital"),
"Abdominal Pain": (1, "icu", "Clinic"),
"Adverse reaction to medication": (1, "icu", "Clinic"),
"Bites and Stings": (1, "icu", "Clinic"),
"Burns/Scalds": (1, "tc", "Clinic"),
"Convulsions/Fitting (not current)": (1, "icu", "Clinic"),
"Eye or vision problems": (1, "icu", "Clinic"),
"Lacerations": (1, "tc", "Clinic"),
"Limb Injury": (1, "tc", "Clinic"),
"Limb Pain (without injury)": (1, "icu", "Clinic"),
"Mental Health Problems": (1, "icu", "Specialized care")
}

def sort(facilitydistances, priority, unit, facility, age):
    rankedHospitals = []
    #maxRange = 20

    #ageCutoff = 17
    #searchCriteria = []
    #if age > ageCutoff:
    #    if symptom_priority >= 2:
    #        searchCriteria[0] = ''


   # if priority > 2:
   #     print("prioritize location")
   # elif priority > 1:
   #     print("prioritize quality")
   # else:
   #     print("closest clinics")
    

    return rankedHospitals