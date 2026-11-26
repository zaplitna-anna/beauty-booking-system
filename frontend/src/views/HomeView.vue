<script setup>
import { ref } from 'vue'
import AboutMaster from '../components/AboutMaster.vue'

const services = ref([
    {
        id: 1,
        name: 'Манікюр',
        description: 'Догляд за нігтями, акуратна форма та красиве покриття.',
        duration: 60,
        price: 500,
        icon: 'fa-solid fa-hand-sparkles',
    },
    {
        id: 2,
        name: 'Педикюр',
        description: 'Професійний догляд для краси та комфорту ваших ніг.',
        duration: 90,
        price: 700,
        icon: 'fa-solid fa-spa',
    },
    {
        id: 3,
        name: 'Оформлення брів',
        description: 'Корекція форми та фарбування для виразного погляду.',
        duration: 45,
        price: 350,
        icon: 'fa-solid fa-wand-magic-sparkles',
    },
])

const steps = [
    {
        number: '01',
        title: 'Обери послугу',
        description: 'Переглянь процедури та знайди потрібну.',
    },
    {
        number: '02',
        title: 'Обери час',
        description: 'Вибери зручну дату та доступну годину.',
    },
    {
        number: '03',
        title: 'Підтвердь запис',
        description: 'Заверши бронювання та переглядай свої записи.',
    },
]
</script>

<template>
    <div class="home-page">
        <AboutMaster />
        <section class="services-section">
            <div class="container">
                <div class="section-heading">
                    <h2>Популярні послуги</h2>
                    <p>
                        Обирай те, що допоможе тобі
                        почуватися ще впевненіше.
                    </p>
                </div>

                <div class="services-grid">
                    <article v-for="service in services" :key="service.id" class="beauty-card">
                        <div class="service-icon">
                            <i :class="service.icon"></i>
                        </div>

                        <h3>{{ service.name }}</h3>
                        <p class="service-description">
                            {{ service.description }}
                        </p>

                        <div class="service-details">
                            <span>
                                <i class="fa-regular fa-clock"></i>
                                {{ service.duration }} хв
                            </span>

                            <strong>{{ service.price }} грн</strong>
                        </div>

                    </article>
                </div>

                <div class="all-services">
                    <RouterLink to="/services" class="secondary-link">
                        Переглянути всі послуги
                    </RouterLink>
                </div>
            </div>
        </section>

        <section id="how-it-works" class="steps-section">
            <div class="container">
                <div class="section-heading">
                    <span class="section-label">ПРОСТО ТА ЗРУЧНО</span>
                    <h2>Як записатися?</h2>
                    <p>Лише три прості кроки.</p>
                </div>

                <div class="steps-grid">
                    <div v-for="step in steps" :key="step.number" class="step-card">
                        <div class="step-number">
                            {{ step.number }}
                        </div>

                        <h3>{{ step.title }}</h3>

                        <p>{{ step.description }}</p>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<style scoped>
.home-page {
    color: var(--dark-color);
}

.container {
    max-width: 1180px;
}

.hero {
    padding: 95px 0;
    background: linear-gradient(135deg,
            #fefafe 0%,
            #f9e9f4 100%);
    overflow: hidden;
}

.hero-layout {
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    align-items: center;
    gap: 70px;
}

.eyebrow,
.section-label {
    display: inline-block;
    color: var(--main-color);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero h1 {
    margin: 22px 0;
    color: var(--dark-color);
    font-family: Georgia, serif;
    font-size: clamp(42px, 5vw, 66px);
    line-height: 1.15;
    font-weight: 600;
}

.hero h1 span {
    display: block;
    color: var(--main-color);
}

.hero-description {
    max-width: 530px;
    color: #695366;
    font-size: 18px;
    line-height: 1.8;
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-top: 32px;
}

.primary-link,
.secondary-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding: 14px 26px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: 600;
    transition: 0.25s ease;
}

.primary-link {
    background: var(--main-color);
    border: 1px solid var(--main-color);
    color: white;
}

.primary-link:hover {
    background: #962878;
    border-color: #962878;
    color: white;
}

.secondary-link {
    background: transparent;
    border: 1px solid var(--main-color);
    color: var(--main-color);
}

.secondary-link:hover {
    background: var(--main-color);
    color: white;
}

.hero-visual {
    position: relative;
    display: flex;
    justify-content: center;
    padding: 35px;
}

.visual-circle {
    position: absolute;
    width: 360px;
    height: 360px;
    border-radius: 50%;
    background: #f1d6e9;
    top: 10px;
    right: 0;
}

.preview-card {
    position: relative;
    z-index: 1;
    width: 100%;
    max-width: 350px;
    padding: 35px;
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 22px;
    box-shadow: 0 18px 45px rgba(70, 2, 51, 0.12);
    text-align: center;
}

.preview-label {
    color: var(--main-color);
    font-size: 11px;
    letter-spacing: 2px;
}

.preview-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 88px;
    height: 88px;
    margin: 25px auto 18px;
    border-radius: 50%;
    background: #f9e9f4;
    color: var(--main-color);
    font-size: 35px;
}

.preview-card h2 {
    font-family: Georgia, serif;
    font-size: 26px;
}

.preview-card>p {
    color: #766174;
    line-height: 1.6;
}

.preview-divider {
    height: 1px;
    margin: 25px 0;
    background: var(--border-color);
}

.preview-detail {
    display: flex;
    align-items: center;
    gap: 13px;
    padding: 9px 0;
    color: #69475d;
    text-align: left;
    font-size: 14px;
}

.preview-detail i {
    width: 20px;
    color: var(--main-color);
}

.services-section,
.steps-section,
.cta-section {
    padding: 85px 0;
}

.section-heading {
    margin-bottom: 45px;
    text-align: center;
}

.section-heading h2,
.cta-content h2 {
    margin: 12px 0;
    font-family: Georgia, serif;
    font-size: clamp(30px, 4vw, 40px);
}

.section-heading p,
.cta-content p {
    color: #766174;
    font-size: 16px;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 25px;
}

.beauty-card {
    display: flex;
    flex-direction: column;
    padding: 30px;
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 18px;
    box-shadow: 0 6px 20px rgba(179, 55, 145, 0.08);
    transition: 0.25s ease;
}

.beauty-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(179, 55, 145, 0.15);
}

.service-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 65px;
    height: 65px;
    margin-bottom: 24px;
    background: #f9e9f4;
    border-radius: 16px;
    color: var(--main-color);
    font-size: 26px;
}

.beauty-card h3 {
    font-size: 22px;
    margin-bottom: 12px;
}

.service-description {
    flex: 1;
    color: #766174;
    line-height: 1.7;
}

.service-details {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    padding: 20px 0;
    margin-top: 12px;
    border-top: 1px solid var(--border-color);
}

.service-details span {
    color: #766174;
}

.service-details strong {
    color: var(--main-color);
}

.service-link {
    display: inline-flex;
    gap: 10px;
    align-items: center;
    color: var(--main-color);
    text-decoration: none;
    font-weight: 600;
}

.service-link:hover {
    color: var(--dark-color);
}

.all-services {
    margin-top: 40px;
    text-align: center;
}

.steps-section {
    background: #f9eef6;
}

.steps-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}

.step-card {
    text-align: center;
    padding: 25px;
}

.step-number {
    margin-bottom: 15px;
    color: var(--main-color);
    font-family: Georgia, serif;
    font-size: 45px;
}

.step-card h3 {
    font-size: 21px;
    margin-bottom: 12px;
}

.step-card p {
    color: #766174;
    line-height: 1.7;
}

.cta-content {
    max-width: 700px;
    margin: 0 auto;
    text-align: center;
}

.cta-content p {
    margin-bottom: 30px;
}

.cta-content .primary-link {
    margin: 0 auto;
}

@media (max-width: 900px) {
    .hero-layout {
        grid-template-columns: 1fr;
        gap: 35px;
    }

    .hero-content {
        text-align: center;
    }

    .hero-description {
        margin-left: auto;
        margin-right: auto;
    }

    .hero-actions {
        justify-content: center;
    }

    .services-grid,
    .steps-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 576px) {
    .hero {
        padding: 55px 0;
    }

    .hero-visual {
        padding: 10px;
    }

    .visual-circle {
        width: 270px;
        height: 270px;
    }

    .preview-card {
        padding: 25px;
    }

    .services-section,
    .steps-section,
    .cta-section {
        padding: 55px 0;
    }

    .beauty-card {
        padding: 24px;
    }
}
</style>
