<script setup>
import { computed } from 'vue'

const props = defineProps({
    booking: {
        type: Object,
        required: true,
    },
    showCustomer: {
        type: Boolean,
        default: false,
    },
})

const statusLabels = {
    CONFIRMED: 'Підтверджено',
    CANCELLED: 'Скасовано',
    PENDING: 'Очікує підтвердження',
}

const statusLabel = computed(
    () => statusLabels[props.booking.status] ?? 'Невідомий статус'
)
</script>

<template>
    <article class="booking-card">
        <div class="card-header">
            <h3>{{ booking.serviceName }}</h3>

            <span class="status-badge" :class="{
                confirmed: booking.status === 'CONFIRMED',
                cancelled: booking.status === 'CANCELLED',
                pending: booking.status === 'PENDING',
            }">
                {{ statusLabel }}
            </span>
        </div>

        <div class="card-divider"></div>

        <div class="booking-details">
            <div class="detail-item">
                <i class="fa-regular fa-calendar"></i>
                <div>
                    <span class="detail-label">Дата візиту</span>
                    <strong>{{ booking.date }}</strong>
                </div>
            </div>

            <div class="detail-item">
                <i class="fa-regular fa-clock"></i>
                <div>
                    <span class="detail-label">Час візиту</span>
                    <strong>
                        {{ booking.startTime }}–{{ booking.endTime }}
                    </strong>
                </div>
            </div>
        </div>

        <div v-if="showCustomer" class="customer-section">
            <div class="card-divider"></div>

            <div class="detail-item">
                <i class="fa-regular fa-user"></i>
                <div>
                    <span class="detail-label">Клієнт</span>
                    <strong>{{ booking.customerName }}</strong>
                </div>
            </div>

            <div class="detail-item">
                <i class="fa-solid fa-phone"></i>
                <div>
                    <span class="detail-label">Телефон</span>
                    <strong>{{ booking.customerPhone }}</strong>
                </div>
            </div>
        </div>
    </article>
</template>

<style scoped>
.booking-card {
    padding: 28px;
    background: white;
    border: 1px solid #f7e1f7;
    border-radius: 18px;
    box-shadow: 0 6px 20px rgba(179, 55, 145, 0.08);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 12px;
}

.card-header h3 {
    margin: 0;
    color: #460233;
    font-size: 21px;
    font-weight: 600;
}

.status-badge {
    padding: 7px 13px;
    border-radius: 30px;
    background: #f3edf1;
    color: #76556c;
    font-size: 12px;
    font-weight: 600;
}

.status-badge.confirmed {
    background: #e6f5e9;
    color: #287345;
}

.status-badge.cancelled {
    background: #f9e5e8;
    color: #a43f57;
}

.status-badge.pending {
    background: #fff1d7;
    color: #956100;
}

.card-divider {
    height: 1px;
    margin: 22px 0;
    background: #f7e1f7;
}

.booking-details {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 20px;
}

.detail-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
}

.detail-item i {
    width: 20px;
    margin-top: 4px;
    color: #b33791;
    font-size: 18px;
}

.detail-item div {
    display: flex;
    flex-direction: column;
    gap: 6px;
    min-width: 0;
}

.detail-label {
    color: #987d90;
    font-size: 13px;
}

.detail-item strong {
    color: #460233;
    font-size: 14px;
    font-weight: 600;
    overflow-wrap: anywhere;
}

.customer-section .detail-item {
    margin-top: 15px;
}

@media (max-width: 576px) {
    .booking-card {
        padding: 22px;
    }

    .booking-details {
        grid-template-columns: 1fr;
    }
}
</style>