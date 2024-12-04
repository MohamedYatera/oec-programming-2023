def determine_symptom_priority(symptom_description, symptom_priority):
    symptoms = symptom_description.split(',')
    priority = 0
    for symptom in symptoms:
        symptom = symptom.strip()
        for symptom_key, symptom_priority_val in symptom_priority.items():
            if symptom in symptom_key:
                priority = max(priority, symptom_priority_val)
    return priority

symptom_priority = {
    "Severe chest or abdominal pain": 10,
    "Difficulty breathing or shortness of breath": 10,
    "bleeding": 10,
    "Sudden or severe injury": 10,
    "Head injury with loss of consciousness or confusion": 10,
    "Signs of a stroke": 10,
    "Severe or persistent vomiting or diarrhea": 10,
    "Poisoning or suspected overdose": 10,
    "High fever or fever with a rash": 10,
    "Seizures or convulsions": 10,
    "Sudden collapse or unexplained fall": 9,
    "Sudden onset of weakness, numbness or paralysis of the face, arm or leg": 9,
    "Suspected severe allergic reaction/ anaphylaxis": 9,
    "Suspected spinal injury": 9,
    "Unconsciousness": 9,
    "Any sudden, severe pain": 8,
    "Anything impaled in any part of the body": 8,
    "Broken bones or dislocated joints": 8,
    "Burns especially to face or genitals": 8,
    "Cuts with exposed tissue": 8,
    "Deep cuts that require sutures": 8,
    "Embedded object in the eye": 8,
    "Flu-like symptoms that are severe or coughing up blood": 8,
    "Head injuries": 8,
    "Inability to urinate": 8,
    "Pain in pregnancy": 8,
    "Persistent high fever despite medication": 8,
    "Pregnancy - reduced movement": 8,
    "Pregnancy - ruptured membranes": 8,
    "Severe testicular pain": 8,
    "Sudden change in mental state or difficulty speaking": 8,
    "Sudden changes in vision": 8,
    "Unusual headaches or migraines": 8,
    "Young children who have stopped drinking or passing urine": 8,
    "Abdominal Pain": 7,
    "Adverse reaction to medication": 7,
    "Bites and Stings": 7,
    "Burns/Scalds": 7,
    "Convulsions/Fitting (not current)": 7,
    "Death of a patient": 7,
    "Eye or vision problems": 7,
    "Fevers (hot to touch) in infants": 7,
    "Lacerations": 7,
    "Limb Injury": 7,
    "Limb Pain (without injury)": 7,
    "Mental Health Problems": 7
}

symptom_description = "Diarrhea, vomiting, stomach cramping, low-grade fever"
priority = determine_symptom_priority(symptom_description, symptom_priority)
print(priority)