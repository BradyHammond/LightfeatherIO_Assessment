<template>
  <div class="registration">
    <v-app>
      <v-content>
        <v-container class="fill-height" fluid>
          <v-row align="center" justify="center">
            <v-col cols="12" sm="10" md="8" lg="6" x-lg="4">
              <v-card class="elevation-12">
                <v-container fluid>
                  <v-row align="center" justify="center">
                    <v-card-title class="pt-8 pb-0 text-center">
                      <img class="d-sm-inline-block logo" src="../../static/images/lightfeather_logo.svg" height="75"/>
                      <span class="display-3 d-inline-block font-weight-medium ml-4 card-title">LightFeather IO</span>
                    </v-card-title>
                  </v-row>
                </v-container>
                <v-card-subtitle class="pt-0">Innovative, Value-Driven IT Solutions</v-card-subtitle>
                  <v-container fluid class="px-10">
                    <v-form ref="form" v-model="valid">
                      <v-text-field v-model="username" :rules="usernameRules" label="Username" placeholder="Username" solo required></v-text-field>
                      <v-text-field v-model="email" :rules="emailRules" label="Email" placeholder="Email" ref="email" solo required></v-text-field>
                      <v-text-field v-model="password" :rules="[() => !!password || 'Please enter a password']" :type="show ? 'text' : 'password'" label="Password" placeholder="Password" :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'" @click:append="show = !show" solo required></v-text-field>
                      <v-text-field v-model="confirmPassword" :rules="[() => password === confirmPassword || 'Passwords do not match']" :type="showAlt ? 'text' : 'password'" label="Confirm Password" placeholder="Confirm Password" :append-icon="showAlt ? 'mdi-eye' : 'mdi-eye-off'" @click:append="showAlt = !showAlt" solo required></v-text-field>
                      <v-btn x-large :disabled="!valid" class="mb-4" id="submit-button" @click.stop="dialog=true">Submit</v-btn>
                    </v-form>
                    <v-dialog v-model="dialog" max-width="290">
                      <v-card>
                        <v-card-title class="text-center d-block">Congratulations</v-card-title>
                        <v-card-text>
                          You have successfully registered with LightFeather IO! At this time, there's nothing more for you to do.
                          We'll be in contact with you shortly.
                        </v-card-text>
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn class="ok-button" text @click="dialog = false">OK</v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                 </v-container>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-content>
    </v-app>
  </div>
</template>

<script>
//Export Registration component
export default {
  name: 'Registration',
  data: () => ({
    show: false,
    showAlt: false,
    dialog: false,
    valid: true,
    username: '',
    usernameRules: [
      v => !!v || 'Please enter a username',
      v => (v && v.length <= 15) || 'Username cannot exceed 15 characters'
    ],
    email: '',
    emailRules: [
      v => !!v || 'Please enter an email',
      v => /^(\(.*\))*(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))(\(.*\))*@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/.test(v) || 'Invalid email'
    ]
  }),
  methods: {
    validate () {
      this.$refs.form.validate()
    }
  }
}
</script>

<style scoped>
.logo {
  vertical-align: middle;
}

.card-title {
  color: #3DC4CC;
  vertical-align: middle;
}

#submit-button {
  background-color: #3DC4CC;
  color: white;
}

.okay-button {
  color: #3DC4CC;
}

@media only screen and (max-width: 650px) {
  .card-title {
    font-size: 1.75em !important;
    margin-left: 8px !important;
  }

  .logo {
    height : 50px;
  }
}

@media only screen and (max-width: 350px) {
  .logo {
    display: none;
  }
}
</style>
