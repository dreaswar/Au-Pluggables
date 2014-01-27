EMAIL_AND_FAX_FORM_CONSTANTS = {
    'email':{
                'max_length': 100,
                "data-dojo-type": "dijit.form.ValidationTextBox",
                "data-dojo-props": r"'required' :'true' ,'regExp':'[\\w]+@.com','invalidMessage':'Invalid Character' "
    },

    'area_code':{
              'max_length': 6,
              "data-dojo-type": "dijit.form.ValidationTextBox",
              "data-dojo-props": r"'required' : 'true' ,'regExp':'[\\d]+','invalidMessage' : 'Invalid Character'"
    },

    'phone':{
              'max_length': 15,
              "data-dojo-type": "dijit.form.ValidationTextBox",
              "data-dojo-props": r"'required' : 'true' ,'regExp':'[\\d]+','invalidMessage' : 'Invalid Character'"
    },

    'phone_type':{
              'max_length': 30,
              "data-dojo-type": "dijit.form.Select",
              "data-dojo-props": r"'required' : 'true' ,'regExp':'[\\w]+','invalidMessage' : 'Invalid Character'"
    },

    'preferred':{
              'max_length': 30,
              "data-dojo-type": "dijit.form.Checkbox",
              "data-dojo-props": r"'required' : false "
    }  
}