CONTACT_FORM_CONSTANTS = {

                  'address_type':{'max_length': 30,
                                  "data-dojo-type": "dijit.form.Select",
                                  "data-dojo-props": r"'required' :'true' ,'regExp':'[\\w]+','invalidMessage':'Invalid Character' "
                  },

                  'address':{'max_length': 1000,
                              "data-dojo-type": "dijit.form.Textarea",
                              "data-dojo-props": r"'required' : 'true' ,'regExp':'[a-zA-Z0-9-:;/\#_]','invalidMessage' : 'Invalid Character'"
                  },

                  'city':{'max_length': 50,
                        "data-dojo-type": "dijit.form.ValidationTextBox",
                        "data-dojo-props": r"'required' : 'true' ,'regExp':'[a-zA-Z -]+','invalidMessage' : 'Invalid Character'"
                  },

                  'state':{'max_length': 50,
                          "data-dojo-type": "dijit.form.ValidationTextBox",
                          "data-dojo-props": r"'required' : 'true' ,'regExp':'[a-zA-Z -]+','invalidMessage' : 'Invalid Character'"
                  },

                  'country':{
                      'max_length': 50,
                      "data-dojo-type": "dijit.form.ValidationTextBox",
                      "data-dojo-props": r"'required' : 'true' ,'regExp':'[\\w]+','invalidMessage' : ''"
                  },

                  'zip_code':{'max_length': 7,
                            "data-dojo-type": "dijit.form.ValidationTextBox",
                            "data-dojo-props": r"'required' : 'true' ,'regExp':'[\\d]+','invalidMessage' : 'Invalid Character'"
                  }
}