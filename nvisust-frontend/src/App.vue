<template>
  <div id="app">
    <nav>
      <router-link to="/">Products</router-link> |
      <router-link to="/order">Place Order</router-link> |
      <router-link to="/history">Order History</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
nav {
  padding: 1rem;
  background-color: #f0f0f0;
}
nav a {
  margin: 0 10px;
}
</style>
