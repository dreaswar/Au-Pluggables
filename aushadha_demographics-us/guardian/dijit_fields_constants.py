GUARDIAN_FORM_CONSTANTS = {

    'guardian_name':{'max_length': 100,
                     "data-dojo-type": "dijit.form.ValidationTextBox",
                     "data-dojo-props": r"'required' :'true' ,'regExp':'[\\w]+','invalidMessage':'Invalid Character' "
                    },

    'relation_to_guardian':{
                        'max_length': 100,
                        "data-dojo-type": "dijit.form.ValidationTextBox",
                        "data-dojo-props": r"'required' : 'true' ,'regExp':'[\\w]+','invalidMessage' : 'Invalid Character'"
                      },

    'next_of_kin':{
                    'max_length': 10,
                    "data-dojo-type": "dijit.form.CheckBox",
                    "data-dojo-props": r"'required' : false "
                    },

    'emergency_contact':{
                      'max_length': 10,
                      "data-dojo-type": "dijit.form.CheckBox",
                      "data-dojo-props": r"'required' : false "
                    },

    'guardian_address':{
                      'max_length': 1000,
                      "data-dojo-type": "dijit.form.SimpleTextarea",
                      "data-dojo-props": r"'required' : true ,'regExp':'[\\w]+','invalidMessage' : 'Invalid Character'"
                      },

    'guardian_city':{
                      'max_length': 30,
                      "data-dojo-type": "dijit.form.ValidationTextBox",
                      "data-dojo-props": r"'required' : true ,'regExp':'[\\w]+','invalidMessage' : 'Invalid Character'"
                    },

    'guardian_state':{
                      'max_length': 30,
                      "data-dojo-type": "dijit.form.ValidationTextBox",
                      "data-dojo-props": r"'required' : true ,'regExp':'[\\w]+','invalidMessage' : 'Invalid Character'"
                    },

    'guardian_country':{
                      'max_length': 30,
                      "data-dojo-type": "dijit.form.ValidationTextBox",
                      "data-dojo-props": r"'required' : true ,'regExp':'[\\w]+','invalidMessage' : 'Invalid Character'"
                    },

    'guardian_zip_code':{
                      'max_length': 20,
                      "data-dojo-type": "dijit.form.ValidationTextBox",
                      "data-dojo-props": r"'required' : true ,'regExp':'[\\d]+','invalidMessage' : 'Invalid Character'"
                    },

    'guardian_phone':{
                      'max_length': 30,
                      "data-dojo-type": "dijit.form.ValidationTextBox",
                      "data-dojo-props": r"'required' : true ,'regExp':'[\\d]+','invalidMessage' : 'Invalid Character'"
                    }

}