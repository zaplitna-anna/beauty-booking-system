<script setup>
import { reactive, ref } from 'vue'

const form = reactive({
    email: '',
    password: '',
})

const showNotice = ref(false)

function submitLogin() {
    showNotice.value = true
}
</script>

<template>
    <section class="auth-shell">
        <div class="auth-card">

            <h1 class="auth-title">З поверненням!</h1>

            <p class="auth-description">
                Увійди до свого кабінету,
                щоб керувати своїми записами.
            </p>

            <form class="beauty-auth-form" @submit.prevent="submitLogin" @input="showNotice = false">
                <div class="form-floating auth-field">
                    <input id="login-email" v-model.trim="form.email" type="email" class="form-control"
                        placeholder="Електронна пошта" autocomplete="email" required />

                    <label for="login-email">
                        Електронна пошта
                    </label>
                </div>

                <div class="form-floating auth-field">
                    <input id="login-password" v-model="form.password" type="password" class="form-control"
                        placeholder="Пароль" autocomplete="current-password" required />

                    <label for="login-password">
                        Пароль
                    </label>
                </div>

                <button type="submit" class="auth-submit">
                    Увійти
                </button>

                <p v-if="showNotice" class="auth-notice" role="status">
                    Це демонстраційна форма входу.
                    Авторизацію через сервер підключимо
                    під час інтеграції.
                </p>
            </form>

            <div class="auth-footer">
                <p>
                    Ще немає облікового запису?
                    <RouterLink to="/register" class="auth-link">
                        Зареєструватися
                    </RouterLink>
                </p>

                <RouterLink to="/" class="back-link">
                    ← На головну
                </RouterLink>
            </div>

        </div>
    </section>
</template>
