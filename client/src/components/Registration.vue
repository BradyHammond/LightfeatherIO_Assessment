<template>
  <div class="registration">
    <v-app>
        <div class="v-card v-card--disabled v-card--raised v-sheet theme--light mx-auto" max-width="500">
          <v-card-title class="mt-2 mx-4">
            <img class="d-none d-sm-block" src="../../static/images/lightfeather_logo.svg" height="75"></img>
            <div class="display-3 font-weight-medium ml-4 card-title">Lightfeather IO</div>
          </v-card-title>
          <v-card-subtitle class="font-weight-medium">Innovative, Value-Driven IT Solutions</v-card-subtitle>
          <v-container fluid class="px-12">
            <v-form ref="form" v-model="valid">
              <v-text-field v-model="username" :rules="usernameRules" label="Username" outlined required></v-text-field>
              <v-text-field v-model="email" :rules="emailRules" label="E-mail" outlined required></v-text-field>
              <v-text-field v-model="password" :rules="passwordRules" type="password" label="Password" outlined required></v-text-field>
              <v-text-field v-model="confirmPassword" :rules="confirmPasswordRules" type="password" label="Confirm Password" outlined required></v-text-field>
              <v-btn x-large disabled class="mb-4" id="submit-button" @click="validate">Submit</v-btn>
            </v-form>
          </v-container>
        </div>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'Registration',
  /*  data() {
    return {
      valid: true,
      username: '',
      usernameRules: [
        v => !!v || 'Please enter a username',
        v => (v && v.length <= 15) || 'Username cannot exceed 15 characters'
      ],
      email: '',
      emailRules: [
        v => !!v || 'Please enter an email',
        v => /.+@.+\..+/.test(v) || 'Invalid email'
      ],
      password: '',
      passwordRules: [
        v => !!V || 'Please enter a password'
      ],
      confirmPassword: '',
      confirmPasswordRules: [
        v => !!V || 'Please re-enter your password',
        password === confirmPassword || 'Passwords do not match'
      ]
    }
  } */
}
</script>

<style scoped>
.registration {
  padding-top: 60px;
}

.card-title {
  color: #3DC4CC;
}

#submit-button {
  background-color: #3DC4CC;
  color: white;
}
</style>
