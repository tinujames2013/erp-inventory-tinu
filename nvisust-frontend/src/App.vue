<template>
  <div>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark px-4">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" to="/">🛠️ ERP Dashboard</RouterLink>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink class="nav-link" to="/">Products</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/order">Place Order</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/history">Order History</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Route Content -->
    <div class="container mt-4">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
// No script needed here for now
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css";

body {
  background-color: #f8f9fa;
  font-family: "Segoe UI", sans-serif;
}

.navbar-brand {
  font-weight: bold;
}
</style>
