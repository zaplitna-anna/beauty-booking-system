<script setup>
const master = {
    name: "Ім'я майстра",
    specialization: 'Майстер краси',
    description:
        'Тут буде коротка розповідь про майстра, ' +
        'його підхід до роботи та послуги, які він пропонує.',
    photo: '',
}
</script>

<template>
    <section id="about-master" class="about-section">
        <div class="about-container">
            <div class="about-layout">

                <div class="about-photo-wrapper">
                    <img v-if="master.photo" :src="master.photo" :alt="`Фото: ${master.name}`" class="master-photo" />

                    <div v-else class="photo-placeholder">
                        <i class="fa-regular fa-user"></i>
                        <span>Тут буде фото майстра</span>
                    </div>
                </div>

                <div class="about-content">
                    <span class="section-label">
                        ЗНАЙОМСТВО З МАЙСТРОМ
                    </span>

                    <h2>
                        Краса починається
                        <span>з турботи</span>
                    </h2>

                    <h3>{{ master.name }}</h3>

                    <p class="specialization">
                        <i class="fa-solid fa-sparkles"></i>
                        {{ master.specialization }}
                    </p>

                    <p class="description">
                        {{ master.description }}
                    </p>

                    <p class="about-message">
                        Beauty Space — місце, де ти можеш
                        обрати процедуру та присвятити час собі.
                    </p>

                    <RouterLink to="/services" class="about-button">
                        Переглянути послуги
                        <i class="fa-solid fa-arrow-right"></i>
                    </RouterLink>
                </div>

            </div>
        </div>
    </section>
</template>

<style scoped>

.about-section {
    padding: 65px 0;
    background: linear-gradient(135deg,
        #FFFAFC 0%,
        #F8EDF2 100%);
}

.about-container {
    width: 100%;
    max-width: 1180px;
    margin: 0 auto;
    padding: 0 20px;
}

.about-layout {
    display: grid;
    grid-template-columns: 0.9fr 1.1fr;
    align-items: center;
    gap: 75px;
}

.about-photo-wrapper {
    width: 100%;
    min-height: 450px;
}

.photo-placeholder,
.master-photo {
    width: 100%;
    height: 450px;
    border-radius: 24px;
}

.photo-placeholder {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 18px;
    background: #F6EAF0;
    border: 1px solid #EEDCE5;
    color: #C18BA3;
}

.photo-placeholder i {
    font-size: 70px;
}

.photo-placeholder span {
    color: #A98B9A;
    font-family: 'Lato', sans-serif;
    font-size: 14px;
}

.master-photo {
    display: block;
    object-fit: cover;
}

.section-label {
    color: #B9829A;
    font-family: 'Lato', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.about-content h2 {
    margin: 20px 0 25px;
    color: #795466;
    font-family: 'Cormorant Infant', serif;
    font-size: clamp(32px, 4vw, 46px);
    font-weight: 600;
    line-height: 1.2;
}

.about-content h2 span {
    display: block;
    color: #B9829A;
}

.about-content h3 {
    margin-bottom: 8px;
    color: #795466;
    font-family: 'Cormorant Infant', serif;
    font-size: 24px;
    font-weight: 600;
}

.specialization {
    color: #B9829A;
    font-family: 'Lato', sans-serif;
    font-size: 15px;
    font-weight: 600;
}

.specialization i {
    margin-right: 8px;
}

.description,
.about-message {
    color: #876F7C;
    font-family: 'Lato', sans-serif;
    font-size: 16px;
    line-height: 1.9;
}

.description {
    margin-top: 25px;
}

.about-message {
    margin-bottom: 30px;
}

.about-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding: 14px 28px;
    background: #C18BA3;
    color: white;
    border-radius: 30px;
    text-decoration: none;
    font-family: 'Lato', sans-serif;
    font-weight: 600;
    transition: background-color 0.2s ease;
}

.about-button:hover {
    background: #A9708C;
    color: white;
}

@media (max-width: 900px) {
    .about-layout {
        grid-template-columns: 1fr;
        gap: 35px;
    }

    .about-photo-wrapper {
        min-height: 350px;
    }

    .photo-placeholder,
    .master-photo {
        height: 350px;
    }

    .about-content {
        order: -1;
    }
}

@media (max-width: 576px) {
    .about-section {
        padding: 55px 0;
    }

    .about-content h2 {
        font-size: 34px;
    }
}

</style>
