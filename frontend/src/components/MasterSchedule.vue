<script setup>
import { computed, reactive, ref } from 'vue'

const weeklySchedule = [
    {
        day: 'Понеділок',
        intervals: [
            { start: '10:00', end: '13:00' },
            { start: '14:00', end: '18:00' },
        ],
    },
    {
        day: 'Вівторок',
        intervals: [{ start: '10:00', end: '18:00' }],
    },
    {
        day: 'Середа',
        intervals: [{ start: '10:00', end: '18:00' }],
    },
    {
        day: 'Четвер',
        intervals: [{ start: '10:00', end: '18:00' }],
    },
    {
        day: "П'ятниця",
        intervals: [{ start: '10:00', end: '17:00' }],
    },
    { day: 'Субота', intervals: [] },
    { day: 'Неділя', intervals: [] },
]

const now = new Date()

const today = [
    now.getFullYear(),
    String(now.getMonth() + 1).padStart(2, '0'),
    String(now.getDate()).padStart(2, '0'),
].join('-')

const selectedDate = ref(today)
const intervals = ref([])
const isDayOff = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const dateOverrides = reactive({})

function getWeekdayIndex(date) {
    const day = new Date(`${date}T12:00:00`).getDay()
    return (day + 6) % 7
}

const selectedWeekday = computed(() => {
    if (!selectedDate.value) return ''

    return weeklySchedule[getWeekdayIndex(selectedDate.value)].day
})

const hasOverride = computed(() =>
    Object.prototype.hasOwnProperty.call(
        dateOverrides,
        selectedDate.value
    )
)

const savedDates = computed(() =>
    Object.keys(dateOverrides).sort()
)

function formatDate(date) {
    return new Date(`${date}T12:00:00`)
        .toLocaleDateString('uk-UA')
}

function formatIntervals(items) {
    if (!items.length) return 'Вихідний'

    return items
        .map((item) => `${item.start}–${item.end}`)
        .join(', ')
}

function loadDateSchedule() {
    errorMessage.value = ''
    successMessage.value = ''

    if (!selectedDate.value) {
        intervals.value = []
        return
    }

    const weekday = weeklySchedule[
        getWeekdayIndex(selectedDate.value)
    ]

    const source = hasOverride.value
        ? dateOverrides[selectedDate.value]
        : weekday.intervals
    intervals.value = source.map((item) => ({ ...item }))
    isDayOff.value = intervals.value.length === 0
}

function addInterval() {
    isDayOff.value = false
    intervals.value.push({ start: '', end: '' })
    errorMessage.value = ''
    successMessage.value = ''
}

function removeInterval(index) {
    intervals.value.splice(index, 1)
    errorMessage.value = ''
    successMessage.value = ''
}

function saveDateSchedule() {
    errorMessage.value = ''
    successMessage.value = ''

    if (!selectedDate.value || selectedDate.value < today) {
        errorMessage.value = 'Оберіть сьогоднішню або майбутню дату.'
        return
    }

    if (isDayOff.value) {
        dateOverrides[selectedDate.value] = []
        successMessage.value = 'Вихідний для цієї дати збережено.'
        return
    }

    if (!intervals.value.length) {
        errorMessage.value =
            'Додайте робочий інтервал або позначте день вихідним.'
        return
    }

    const sorted = intervals.value
        .map((item) => ({ ...item }))
        .sort((a, b) => a.start.localeCompare(b.start))

    for (let i = 0; i < sorted.length; i++) {
        if (
            !sorted[i].start ||
            !sorted[i].end ||
            sorted[i].start >= sorted[i].end
        ) {
            errorMessage.value = 'Перевірте початок і кінець інтервалів.'
            return
        }

        if (i > 0 && sorted[i].start < sorted[i - 1].end) {
            errorMessage.value = 'Робочі інтервали не повинні перетинатися.'
            return
        }
    }

    dateOverrides[selectedDate.value] = sorted
    intervals.value = sorted.map((item) => ({ ...item }))

    successMessage.value = 'Графік для вибраної дати збережено.'
}

function resetDateSchedule() {
    delete dateOverrides[selectedDate.value]
    loadDateSchedule()
    successMessage.value = 'Відновлено звичайний графік цього дня.'
}

function chooseSavedDate(date) {
    selectedDate.value = date
    loadDateSchedule()
}

loadDateSchedule()
</script>

<template>
    <section class="master-schedule">
        <div class="section-heading">
            <span class="section-label">РОБОЧИЙ ЧАС</span>
            <h2>Мій графік</h2>

            <p>
                Переглядай звичайний графік та налаштовуй
                окремі дати для запису клієнтів.
            </p>
        </div>

        <div class="schedule-block">
            <h3>Звичайний тижневий графік</h3>

            <div class="weekly-list">
                <div v-for="item in weeklySchedule" :key="item.day" class="weekly-row">
                    <strong>{{ item.day }}</strong>
                    <span>{{ formatIntervals(item.intervals) }}</span>
                </div>
            </div>
        </div>

        <div class="schedule-block">
            <h3>Налаштувати конкретну дату</h3>

            <p class="hint">
                Наприклад, можна змінити години через два
                чи три тижні, не змінюючи інші дні.
            </p>

            <label class="field-label" for="schedule-date">
                Обери дату
            </label>

            <input id="schedule-date" v-model="selectedDate" type="date" :min="today" class="date-input"
                @change="loadDateSchedule" />

            <p class="selected-day" v-if="selectedDate">
                {{ selectedWeekday }}, {{ formatDate(selectedDate) }}
                <span v-if="hasOverride">· Індивідуальний графік</span>
                <span v-else>· Звичайний графік</span>
            </p>

            <label class="day-off-option">
                <input v-model="isDayOff" type="checkbox" @change="errorMessage = ''; successMessage = ''" />
                Зробити цей день вихідним
            </label>

            <div v-if="!isDayOff" class="intervals-section">
                <h4>Робочі інтервали</h4>

                <div v-for="(interval, index) in intervals" :key="index" class="interval-row">
                    <label>
                        Початок
                        <input v-model="interval.start" type="time" @input="errorMessage = ''; successMessage = ''" />
                    </label>

                    <label>
                        Кінець
                        <input v-model="interval.end" type="time" @input="errorMessage = ''; successMessage = ''" />
                    </label>

                    <button type="button" class="remove-button" @click="removeInterval(index)"
                        :aria-label="`Видалити інтервал ${index + 1}`">
                        <i class="fa-solid fa-trash"></i>
                    </button>
                </div>

                <button type="button" class="outline-button" @click="addInterval">
                    <i class="fa-solid fa-plus"></i>
                    Додати інтервал
                </button>
            </div>

            <p v-if="errorMessage" class="error-message" role="alert">
                {{ errorMessage }}
            </p>

            <p v-if="successMessage" class="success-message" role="status">
                {{ successMessage }}
            </p>

            <div class="schedule-actions">
                <button type="button" class="save-button" @click="saveDateSchedule">
                    Зберегти графік дати
                </button>

                <button v-if="hasOverride" type="button" class="outline-button" @click="resetDateSchedule">
                    Відновити звичайний графік
                </button>
            </div>
        </div>

        <div v-if="savedDates.length" class="schedule-block">
            <h3>Змінені дати</h3>

            <div v-for="date in savedDates" :key="date" class="override-row">
                <div>
                    <strong>{{ formatDate(date) }}</strong>
                    <p>{{ formatIntervals(dateOverrides[date]) }}</p>
                </div>

                <button type="button" class="outline-button" @click="chooseSavedDate(date)">
                    Переглянути
                </button>
            </div>
        </div>

        <p class="demo-message">
            Це демонстраційне налаштування для ЛР №4.
            Зміни зберігаються тільки в пам'яті сторінки
            та зникнуть після її перезавантаження.
        </p>
    </section>
</template>

<style scoped>
.master-schedule {
    color: #460233;
}

.section-label {
    color: #b33791;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.section-heading h2 {
    margin: 10px 0;
    font-family: Georgia, serif;
    font-size: 28px;
}

.section-heading p,
.hint {
    color: #76556c;
    line-height: 1.7;
}

.schedule-block {
    margin-top: 28px;
    padding: 24px;
    border: 1px solid #f7e1f7;
    border-radius: 16px;
    background: #fff;
}

.schedule-block h3 {
    margin-bottom: 20px;
    color: #460233;
    font-size: 19px;
}

.weekly-list {
    display: grid;
    gap: 0;
}

.weekly-row,
.override-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    padding: 14px 0;
    border-bottom: 1px solid #f7e1f7;
}

.weekly-row:last-child,
.override-row:last-child {
    border-bottom: none;
}

.weekly-row strong,
.override-row strong {
    color: #460233;
}

.weekly-row span,
.override-row p {
    color: #76556c;
    font-size: 14px;
}

.override-row p {
    margin: 5px 0 0;
}

.field-label {
    display: block;
    margin: 20px 0 10px;
    font-weight: 600;
}

.date-input,
.interval-row input {
    padding: 11px;
    border: 1px solid #e5cddb;
    border-radius: 10px;
    background: white;
    color: #460233;
}

.date-input {
    width: 100%;
    max-width: 300px;
}

.selected-day {
    margin: 14px 0;
    color: #76556c;
    font-size: 14px;
}

.selected-day span {
    color: #b33791;
}

.day-off-option {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 22px 0;
    cursor: pointer;
}

.day-off-option input {
    accent-color: #b33791;
}

.intervals-section h4 {
    font-size: 16px;
    margin-bottom: 15px;
}

.interval-row {
    display: flex;
    align-items: end;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 14px;
}

.interval-row label {
    display: flex;
    flex-direction: column;
    gap: 7px;
    color: #76556c;
    font-size: 13px;
}

.schedule-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 25px;
}

.save-button,
.outline-button,
.remove-button {
    border-radius: 30px;
    padding: 11px 18px;
    font-weight: 600;
    cursor: pointer;
}

.save-button {
    background: #b33791;
    border: 1px solid #b33791;
    color: white;
}

.save-button:hover {
    background: #962878;
}

.outline-button {
    background: white;
    border: 1px solid #b33791;
    color: #b33791;
}

.outline-button:hover {
    background: #f9e9f4;
}

.remove-button {
    border: 1px solid #f1d1dc;
    background: #fff;
    color: #a43f57;
}

.error-message {
    color: #a43f57;
}

.success-message {
    color: #287345;
}

.demo-message {
    margin: 25px 0 0;
    padding: 15px;
    background: #f9eef6;
    border-radius: 10px;
    color: #76556c;
    font-size: 13px;
}

@media (max-width: 576px) {
    .schedule-block {
        padding: 18px;
    }

    .weekly-row {
        align-items: flex-start;
        flex-direction: column;
    }
}
</style>