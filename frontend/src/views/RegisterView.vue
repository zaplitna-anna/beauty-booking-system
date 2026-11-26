<script setup>
import { reactive, ref } from 'vue'

const form = reactive({
    name: '',
    last_name: '',
    phone: '',
    email: '',
    password: '',
})

const confirmPassword = ref('')
const errorMessage = ref('')
const showNotice = ref(false)

function formatPhone(value) {
    let digits = value.replace(/\D/g, '')
    if (digits.startsWith('380')) {
        digits = digits.slice(3)
    } else if (digits.startsWith('0')) {
        digits = digits.slice(1)
    }
    digits = digits.slice(0, 9)
    let result = '+380'

    if (digits.length > 0) {
        result += ` (${digits.slice(0, 2)}`
    }

    if (digits.length >= 2) {
        result += ')'
    }

    if (digits.length > 2) {
        result += ` ${digits.slice(2, 5)}`
    }

    if (digits.length > 5) {
        result += `-${digits.slice(5, 7)}`
    }

    if (digits.length > 7) {
        result += `-${digits.slice(7, 9)}`
    }

    return result
}


function updatePhone(event) {
    const formatted = formatPhone(event.target.value)

    form.phone = formatted
    event.target.value = formatted
}



function resetFeedback() {
    errorMessage.value = ''
    showNotice.value = false
}

function submitRegistration() {
    errorMessage.value = ''

    if (form.password !== confirmPassword.value) {
        errorMessage.value = 'Паролі не збігаються.'
        return
    }

    showNotice.value = true
}
</script>

<template>
    <section class="auth-shell">
        <div class="auth-card register-card">

            <h1 class="auth-title">Створи свій акаунт</h1>

            <p class="auth-description">
                Зареєструйся, щоб у майбутньому
                записуватися на процедури онлайн
                та переглядати свої бронювання.
            </p>

            <form class="beauty-auth-form" @submit.prevent="submitRegistration" @input="resetFeedback">
                <div class="form-floating auth-field">
                    <input id="register-name" v-model.trim="form.name" type="text" class="form-control"
                        placeholder="Ім'я" autocomplete="given-name" required />
                    <label for="register-name">Ім'я</label>
                </div>
                <div class="form-floating auth-field">
                    <input id="register-last-name" v-model.trim="form.last_name" type="text" class="form-control"
                        placeholder="Прізвище" autocomplete="family-name" required />

                    <label for="register-last-name">
                        Прізвище
                    </label>
                </div>
                <div class="form-floating auth-field">
                <input
                    id="register-phone"
                    :value="form.phone"
                    @input="updatePhone"
                    type="tel"
                    class="form-control"
                    placeholder="+380 (XX) XXX-XX-XX"
                    pattern="\+380 \([0-9]{2}\) [0-9]{3}-[0-9]{2}-[0-9]{2}"
                    title="Введіть номер у форматі +380 (XX) XXX-XX-XX"
                    autocomplete="tel"
                    required
                />

                <label for="register-phone">
                    Номер телефону
                </label>
                </div>

                <div class="form-floating auth-field">
                    <input id="register-email" v-model.trim="form.email" type="email" class="form-control"
                        placeholder="Електронна пошта" autocomplete="email" required />

                    <label for="register-email">
                        Електронна пошта
                    </label>
                </div>

                <div class="form-floating auth-field">
                    <input id="register-password" v-model="form.password" type="password" class="form-control"
                        placeholder="Пароль" minlength="8" autocomplete="new-password" required />

                    <label for="register-password">
                        Пароль (від 8 символів)
                    </label>
                </div>

                <div class="form-floating auth-field">
                    <input id="register-confirm-password" v-model="confirmPassword" type="password" class="form-control"
                        placeholder="Повторіть пароль" minlength="8" autocomplete="new-password" required />

                    <label for="register-confirm-password">
                        Повторіть пароль
                    </label>
                </div>

                <p v-if="errorMessage" class="auth-error" role="alert">
                    {{ errorMessage }}
                </p>

                <button type="submit" class="auth-submit">
                    Зареєструватися
                </button>

                <p v-if="showNotice" class="auth-notice" role="status">
                    Форму заповнено правильно.
                    Це демонстраційна реєстрація:
                    обліковий запис ще не створено.
                </p>
            </form>

            <div class="auth-footer">
                <p>
                    Уже маєш обліковий запис?
                    <RouterLink to="/login" class="auth-link">
                        Увійти
                    </RouterLink>
                </p>

                <RouterLink to="/" class="back-link">
                    ← На головну
                </RouterLink>
            </div>

        </div>
    </section>
</template>
