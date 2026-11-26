<script setup>
import { computed, ref } from 'vue'

const categories = [
    'Усі послуги',
    'Нігті',
    'Брови',
    'Вії',
]

const selectedCategory = ref('Усі послуги')

const services = [
    {
        id: 1,
        name: 'Манікюр',
        category: 'Нігті',
        description:
            'Догляд за нігтями, акуратна форма та охайний вигляд рук.',
        duration: 60,
        price: 500,
        icon: 'fa-solid fa-hand-sparkles',
    },
    {
        id: 2,
        name: 'Манікюр із покриттям',
        category: 'Нігті',
        description:
            'Манікюр із нанесенням стійкого декоративного покриття.',
        duration: 90,
        price: 650,
        icon: 'fa-solid fa-paintbrush',
    },
    {
        id: 3,
        name: 'Педикюр',
        category: 'Нігті',
        description:
            'Комплексний догляд за стопами та нігтями.',
        duration: 90,
        price: 700,
        icon: 'fa-solid fa-spa',
    },
    {
        id: 4,
        name: 'Оформлення брів',
        category: 'Брови',
        description:
            'Корекція форми та фарбування для виразного погляду.',
        duration: 45,
        price: 350,
        icon: 'fa-solid fa-wand-magic-sparkles',
    },
    {
        id: 5,
        name: 'Корекція брів',
        category: 'Брови',
        description:
            'Надання бровам гармонійної форми з урахуванням рис обличчя.',
        duration: 30,
        price: 300,
        icon: 'fa-solid fa-feather',
    },
    {
        id: 6,
        name: 'Ламінування вій',
        category: 'Вії',
        description:
            'Процедура для виразного вигину та доглянутого вигляду вій.',
        duration: 60,
        price: 600,
        icon: 'fa-solid fa-eye',
    },
]

const filteredServices = computed(() => {
    if (selectedCategory.value === 'Усі послуги') {
        return services
    }

    return services.filter(
        (service) => service.category === selectedCategory.value
    )
})
</script>

<template>
    <div class="services-page">
        <section class="services-hero">
            <div class="page-container">
                <h1>Твій час для краси</h1>
                <p>
                    Обирай улюблені процедури, знайомся з послугами
                    та плануй свій час для краси.
                </p>
            </div>
        </section>
        <section class="catalog-section">
            <div class="page-container">

                <div class="catalog-heading">
                    <div>
                        <span class="section-label">ОБИРАЙ ДЛЯ СЕБЕ</span>
                        <h2>Послуги</h2>
                    </div>

                    <span class="services-count">
                        Знайдено послуг: {{ filteredServices.length }}
                    </span>
                </div>
                <div class="category-filters">
                    <button v-for="category in categories" :key="category" type="button" class="filter-button"
                        :class="{ active: selectedCategory === category }" :aria-pressed="selectedCategory === category"
                        @click="selectedCategory = category">
                        {{ category }}
                    </button>
                </div>
                <div class="services-grid">
                    <article v-for="service in filteredServices" :key="service.id" class="service-card">
                        <div class="card-top">
                            <div class="service-icon">
                                <i :class="service.icon"></i>
                            </div>

                            <span class="category-badge">
                                {{ service.category }}
                            </span>
                        </div>

                        <h3>{{ service.name }}</h3>

                        <p class="service-description">
                            {{ service.description }}
                        </p>

                        <div class="service-info">
                            <div class="info-item">
                                <i class="fa-regular fa-clock"></i>
                                <span>{{ service.duration }} хв</span>
                            </div>

                            <div class="service-price">
                                {{ service.price }} грн
                            </div>
                        </div>

                        <RouterLink to="/booking" class="booking-button">
                            Записатися
                            <i class="fa-solid fa-arrow-right"></i>
                        </RouterLink>
                    </article>
                </div>

                <p v-if="filteredServices.length === 0" class="empty-message">
                    У цій категорії поки немає послуг.
                </p>

                <p class="demo-notice">
                    Послуги та ціни наведено для демонстрації.
                    Актуальні дані завантажуватимуться із сервера
                    після інтеграції.
                </p>
            </div>
        </section>

        <section class="services-bottom">
            <div class="page-container">
                <div class="bottom-content">
                    <span class="section-label">
                        ЧАС ДЛЯ СЕБЕ
                    </span>
                    <h2>Подаруй собі момент турботи</h2>
                    <p>
                        Обери процедуру, що тобі до душі,
                        та заплануй свій наступний візит.
                    </p>
                    <RouterLink to="/booking" class="bottom-button">
                        Перейти до запису
                    </RouterLink>
                </div>
            </div>
        </section>
    </div>
</template>

<style scoped>
.services-page {
    color: var(--dark-color);
}

.page-container {
    width: 100%;
    max-width: 1180px;
    margin: 0 auto;
    padding: 0 20px;
}

.services-hero {
    padding: 85px 20px;
    text-align: center;
    background: linear-gradient(135deg,
            #fefafe 0%,
            #f9e9f4 100%);
}

.section-label {
    color: var(--main-color);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.services-hero h1 {
    margin: 18px 0;
    color: var(--dark-color);
    font-family: Georgia, serif;
    font-size: clamp(36px, 5vw, 54px);
    font-weight: 600;
}

.services-hero p {
    max-width: 650px;
    margin: 0 auto;
    color: #76556c;
    font-size: 17px;
    line-height: 1.8;
}

.catalog-section {
    padding: 70px 0 90px;
}

.catalog-heading {
    display: flex;
    justify-content: space-between;
    align-items: end;
    flex-wrap: wrap;
    gap: 15px;
    margin-bottom: 28px;
}

.catalog-heading h2 {
    margin: 10px 0 0;
    color: var(--dark-color);
    font-family: Georgia, serif;
    font-size: 36px;
}

.services-count {
    color: #76556c;
    font-size: 14px;
}

.category-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 35px;
}

.filter-button {
    padding: 10px 22px;
    border: 1px solid var(--border-color);
    border-radius: 30px;
    background: white;
    color: #69475d;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: 0.25s ease;
}

.filter-button:hover {
    color: var(--main-color);
    border-color: var(--main-color);
}

.filter-button.active {
    background: var(--main-color);
    border-color: var(--main-color);
    color: white;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 25px;
}

.service-card {
    display: flex;
    flex-direction: column;
    min-width: 0;
    padding: 28px;
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 18px;
    box-shadow: 0 6px 20px rgba(179, 55, 145, 0.08);
    transition: 0.25s ease;
}

.service-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(179, 55, 145, 0.15);
}

.card-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 22px;
}

.service-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 68px;
    height: 68px;
    border-radius: 17px;
    background: #f9e9f4;
    color: var(--main-color);
    font-size: 26px;
}

.category-badge {
    padding: 6px 12px;
    border-radius: 20px;
    background: #f9eef6;
    color: var(--main-color);
    font-size: 12px;
    font-weight: 600;
}

.service-card h3 {
    margin-bottom: 13px;
    color: var(--dark-color);
    font-size: 22px;
    font-weight: 600;
}

.service-description {
    flex: 1;
    min-height: 72px;
    color: #76556c;
    font-size: 15px;
    line-height: 1.7;
}

.service-info {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    margin-top: 18px;
    padding: 20px 0;
    border-top: 1px solid var(--border-color);
}

.info-item {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #76556c;
    font-size: 14px;
}

.info-item i {
    color: var(--main-color);
}

.service-price {
    color: var(--main-color);
    font-size: 20px;
    font-weight: 700;
}

.booking-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding: 13px 20px;
    border-radius: 30px;
    background: var(--main-color);
    color: white;
    text-decoration: none;
    font-weight: 600;
    transition: 0.25s ease;
}

.booking-button:hover {
    background: #962878;
    color: white;
}

.empty-message {
    padding: 25px;
    text-align: center;
    color: #76556c;
}

.demo-notice {
    margin-top: 30px;
    color: #95778a;
    font-size: 13px;
    text-align: center;
}

.services-bottom {
    padding: 80px 0;
    background: #f9eef6;
}

.bottom-content {
    max-width: 650px;
    margin: 0 auto;
    text-align: center;
}

.bottom-content h2 {
    margin: 15px 0;
    color: var(--dark-color);
    font-family: Georgia, serif;
    font-size: clamp(30px, 4vw, 40px);
}

.bottom-content p {
    margin-bottom: 28px;
    color: #76556c;
    line-height: 1.8;
}

.bottom-button {
    display: inline-block;
    padding: 14px 28px;
    border-radius: 30px;
    background: var(--main-color);
    color: white;
    text-decoration: none;
    font-weight: 600;
}

.bottom-button:hover {
    background: #962878;
    color: white;
}

@media (max-width: 992px) {
    .services-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 600px) {
    .services-hero {
        padding: 55px 0;
    }

    .catalog-section,
    .services-bottom {
        padding-top: 55px;
        padding-bottom: 55px;
    }

    .services-grid {
        grid-template-columns: 1fr;
    }

    .catalog-heading h2 {
        font-size: 30px;
    }

    .service-card {
        padding: 24px;
    }

    .category-filters {
        gap: 8px;
    }

    .filter-button {
        padding: 9px 15px;
    }
}
</style>
