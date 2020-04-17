<template>
  <div class="notFound">
    <v-app>
      <div class="content">
        <div class="display-4 font-weight-bold">Oh No!</div>
        <div class="title">We can't seem to find the page you're looking for.</div>
        <div class="sub-title-1">Error code: 404</div>
      </div>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
  data () {
    return {}
  }
}
</script>

<style scoped>
.content {
  margin-top: 200px;
}
</style>
