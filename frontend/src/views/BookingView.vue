<script setup>
import { computed, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const services = [
    { id: 1, name: 'Манікюр', duration: 60, price: 500 },
    { id: 2, name: 'Манікюр із покриттям', duration: 90, price: 650 },
    { id: 3, name: 'Педикюр', duration: 90, price: 700 },
    { id: 4, name: 'Оформлення брів', duration: 45, price: 350 },
    { id: 5, name: 'Корекція брів', duration: 30, price: 300 },
    { id: 6, name: 'Ламінування вій', duration: 60, price: 600 },
]

const timeSlots = [
    '09:00',
    '10:30',
    '12:00',
    '14:00',
    '15:30',
    '17:00',
]

const now = new Date()
const today = [
    now.getFullYear(),
    String(now.getMonth() + 1).padStart(2, '0'),
    String(now.getDate()).padStart(2, '0'),
].join('-')

const serviceFromUrl = String(route.query.service ?? '')

const selectedServiceId = ref(
    services.some((service) => String(service.id) === serviceFromUrl)
        ? serviceFromUrl
        : ''
)

const selectedDate = ref('')
const selectedTime = ref('')
const showNotice = ref(false)

const selectedService = computed(() =>
    services.find(
        (service) => String(service.id) === selectedServiceId.value
    )
)

const formattedDate = computed(() => {
    if (!selectedDate.value) {
        return 'Не обрано'
    }

    return new Date(
        `${selectedDate.value}T12:00:00`
    ).toLocaleDateString('uk-UA')
})

const canSubmit = computed(
    () =>
        selectedService.value &&
        selectedDate.value >= today &&
        selectedTime.value
)

function resetSelection() {
    selectedTime.value = ''
    showNotice.value = false
}

function submitBooking() {
    if (!canSubmit.value) {
        return
    }
    showNotice.value = true
}
</script>

<template>
    <div class="booking-page">
        <section class="booking-hero">
            <div class="page-container">
                <h1>Запис на процедуру</h1>
                <p>
                    Обери послугу та зручний час
                    для свого візиту до майстра.
                </p>
            </div>
        </section>
        <section class="booking-section">
            <div class="page-container">
                <div class="booking-layout">
                    <form class="booking-form" @submit.prevent="submitBooking">
                        <h2>Деталі запису</h2>
                        <div class="form-group">
                            <label for="booking-service">
                                <span class="step-number">01</span>
                                Обери послугу
                            </label>

                            <select id="booking-service" v-model="selectedServiceId" required @change="resetSelection">
                                <option value="" disabled>
                                    Оберіть послугу
                                </option>

                                <option v-for="service in services" :key="service.id" :value="String(service.id)">
                                    {{ service.name }} — {{ service.price }} грн
                                </option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="booking-date">
                                <span class="step-number">02</span>
                                Обери дату
                            </label>

                            <input id="booking-date" v-model="selectedDate" type="date" :min="today" required
                                @change="resetSelection" />

                            <p class="field-hint">
                                Обери дату, на яку хочеш записатися.
                            </p>
                        </div>

                        <fieldset class="time-fieldset">
                            <legend>
                                <span class="step-number">03</span>
                                Обери час
                            </legend>

                            <p class="field-hint">
                                Наведені години - приклад інтерфейсу.
                                Реальну доступність підключимо пізніше.
                            </p>

                            <div class="time-grid">
                                <button v-for="time in timeSlots" :key="time" type="button" class="time-button"
                                    :class="{ active: selectedTime === time }" :aria-pressed="selectedTime === time"
                                    :disabled="!selectedService || !selectedDate"
                                    @click="selectedTime = time; showNotice = false">
                                    {{ time }}
                                </button>
                            </div>
                        </fieldset>

                        <button type="submit" class="submit-button" :disabled="!canSubmit">
                            Переглянути вибір
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>

                        <p v-if="showNotice" class="booking-notice" role="status">
                            Ваш вибір готовий до перегляду.
                            Це демонстраційна форма: запис ще
                            не створено та не збережено.
                        </p>
                    </form>

                    <aside class="booking-summary">
                        <h2>Ваш запис</h2>
                        <div class="summary-divider"></div>
                        <div class="summary-item">
                            <span>Послуга</span>
                            <strong>
                                {{ selectedService?.name || 'Не обрано' }}
                            </strong>
                        </div>

                        <div class="summary-item">
                            <span>Дата</span>
                            <strong>{{ formattedDate }}</strong>
                        </div>

                        <div class="summary-item">
                            <span>Час</span>
                            <strong>{{ selectedTime || 'Не обрано' }}</strong>
                        </div>

                        <div class="summary-item">
                            <span>Тривалість</span>
                            <strong>
                                {{
                                    selectedService
                                        ? `${selectedService.duration} хв`
                                        : '—'
                                }}
                            </strong>
                        </div>

                        <div class="summary-divider"></div>

                        <div class="summary-total">
                            <span>Вартість</span>

                            <strong>
                                {{
                                    selectedService
                                        ? `${selectedService.price} грн`
                                        : '—'
                                }}
                            </strong>
                        </div>

                        <p class="summary-note">
                            <i class="fa-solid fa-circle-info"></i>
                            Ціни та години наведено для демонстрації.
                            Підтвердження справжнього запису
                            додамо після інтеграції з сервером.
                        </p>
                    </aside>
                </div>
            </div>
        </section>
    </div>
</template>

<style scoped>
.booking-page {
    color: var(--dark-color);
}

.page-container {
    max-width: 1180px;
    margin: 0 auto;
    padding: 0 20px;
}

.booking-hero {
    padding: 70px 0;
    background: linear-gradient(135deg,
            #fefafe 0%,
            #f9e9f4 100%);
    text-align: center;
}

.section-label {
    color: var(--main-color);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.booking-hero h1 {
    margin: 18px 0;
    color: var(--dark-color);
    font-family: Georgia, serif;
    font-size: clamp(34px, 5vw, 52px);
}

.booking-hero p {
    color: #76556c;
    font-size: 17px;
}

.booking-section {
    padding: 70px 0 90px;
}

.booking-layout {
    display: grid;
    grid-template-columns: minmax(0, 1.3fr) minmax(0, 0.85fr);
    align-items: start;
    gap: 30px;
}

.booking-form,
.booking-summary {
    padding: 35px;
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 20px;
    box-shadow: 0 6px 20px rgba(179, 55, 145, 0.07);
}

.booking-form h2,
.booking-summary h2 {
    margin: 0 0 30px;
    color: var(--dark-color);
    font-family: Georgia, serif;
    font-size: 27px;
}

.form-group {
    margin-bottom: 30px;
}

.form-group label,
.time-fieldset legend {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 15px;
    color: var(--dark-color);
    font-weight: 600;
    font-size: 16px;
}

.step-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex: 0 0 34px;
    height: 34px;
    background: #f9e9f4;
    color: var(--main-color);
    border-radius: 50%;
    font-size: 13px;
}

.form-group select,
.form-group input {
    display: block;
    width: 100%;
    min-height: 48px;
    padding: 12px 15px;
    border: 1px solid #e5cddb;
    border-radius: 10px;
    background: white;
    color: var(--dark-color);
    font-size: 15px;
}

.form-group select:focus,
.form-group input:focus {
    outline: 2px solid rgba(179, 55, 145, 0.25);
    border-color: var(--main-color);
}

.field-hint {
    margin: 10px 0 0;
    color: #987d90;
    font-size: 13px;
    line-height: 1.6;
}

.time-fieldset {
    min-width: 0;
    margin: 0 0 30px;
    padding: 0;
    border: none;
}

.time-fieldset legend {
    width: 100%;
    float: none;
}

.time-fieldset .field-hint {
    margin-bottom: 18px;
}

.time-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
}

.time-button {
    padding: 12px;
    background: white;
    border: 1px solid var(--main-color);
    border-radius: 10px;
    color: var(--main-color);
    font-weight: 600;
    cursor: pointer;
}

.time-button:hover:not(:disabled),
.time-button.active {
    background: var(--main-color);
    color: white;
}

.time-button:disabled {
    opacity: 0.4;
    cursor: not-allowed;
}

.submit-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    width: 100%;
    padding: 15px;
    border: none;
    border-radius: 30px;
    background: var(--main-color);
    color: white;
    font-weight: 600;
    cursor: pointer;
}

.submit-button:hover:not(:disabled) {
    background: #962878;
}

.submit-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.booking-notice {
    margin-top: 18px;
    padding: 15px;
    background: #f9eef6;
    border-radius: 10px;
    color: #87385f;
    font-size: 14px;
}

.summary-subtitle {
    color: var(--main-color);
    font-size: 14px;
}

.summary-subtitle i {
    margin-right: 7px;
}

.summary-divider {
    height: 1px;
    margin: 25px 0;
    background: var(--border-color);
}

.summary-item {
    display: flex;
    justify-content: space-between;
    gap: 15px;
    margin-bottom: 20px;
    font-size: 14px;
}

.summary-item span {
    color: #987d90;
}

.summary-item strong {
    color: var(--dark-color);
    text-align: right;
}

.summary-total {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
}

.summary-total span {
    color: var(--dark-color);
    font-weight: 600;
}

.summary-total strong {
    color: var(--main-color);
    font-size: 26px;
}

.summary-note {
    margin: 30px 0 0;
    padding: 15px;
    background: #f9eef6;
    border-radius: 10px;
    color: #76556c;
    font-size: 13px;
    line-height: 1.7;
}

.summary-note i {
    color: var(--main-color);
    margin-right: 5px;
}

@media (max-width: 900px) {
    .booking-layout {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 576px) {
    .booking-hero {
        padding: 55px 0;
    }

    .booking-section {
        padding: 40px 0 60px;
    }

    .booking-form,
    .booking-summary {
        padding: 24px;
    }

    .time-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}
</style>
