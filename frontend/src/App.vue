<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="app-layout">
    <header class="site-header sticky-top">
      <div class="container header-content">
        <RouterLink to="/" class="brand">
          <span class="brand-name">
            Beauty Space
            <small>Твій простір краси</small>
          </span>
        </RouterLink>

        <nav class="main-nav">
          <RouterLink to="/">Головна</RouterLink>
          <RouterLink to="/services">Послуги</RouterLink>
          <RouterLink to="/booking">Записатися</RouterLink>
        </nav>

        <div class="account-actions">
          <RouterLink to="/login" class="btn btn-outline-primary rounded-pill px-4">
            Вхід
          </RouterLink>
          <RouterLink to="/register" class="btn btn-primary rounded-pill px-4">
            Реєстрація
          </RouterLink>
        </div>
      </div>
    </header>

    <main class="page-content">
      <RouterView />
    </main>

    <footer class="site-footer">
      <p>Beauty Space — твій простір краси</p>
    </footer>
  </div>
</template>

<style scoped>
.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.site-header {
  background: #fffcfd;
  border-bottom: 1px solid #eedce5;
  box-shadow: 0 2px 12px rgba(121, 84, 102, 0.06);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 20px;
  padding-top: 16px;
  padding-bottom: 16px;
}

.brand {
  display: inline-flex;
  align-items: center;
  text-decoration: none;
}

.brand-name {
  display: flex;
  flex-direction: column;
  color: #795466;
  font-family: 'Parisienne', cursive;
  font-size: 30px;
  font-weight: 400;
  line-height: 1.2;
}

.brand-name small {
  margin-top: 4px;
  color: #b9829a;
  font-family: 'Lato', sans-serif;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 1.8px;
  text-transform: uppercase;
}

.main-nav,
.account-actions {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 15px;
}

.main-nav a {
  color: #b9829a;
  font-family: 'Lato', sans-serif;
  text-decoration: none;
  font-weight: 500;
}

.main-nav a:hover,
.main-nav a.router-link-exact-active {
  color: #795466;
}

.page-content {
  flex: 1;
}

.site-footer {
  padding: 25px 15px;
  background: #795466;
  text-align: center;
}

.site-footer p {
  margin: 0;
  color: white;
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    align-items: center;
  }

  .main-nav {
    justify-content: center;
  }
}
</style>
