<template>
    <div class="main">
        <div class="window">
            <slot></slot>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    data() {
        return {
            
        }
    }
});
</script>
<style lang="scss">
@keyframes load {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.main {
    display: flex;
    align-items: center;
    justify-content: center;
}

.window {
    box-shadow: rgba(0, 0, 0, 0.2) 0 0 10px;
    background-color: rgba(0, 0, 0, 0.192);
    backdrop-filter: blur(10px) saturate(1.5);
    border-radius: 20px;
    width: calc(100% - 2rem);
    height: calc(100% - 2rem);
    // overflow-y: overlay;
    animation-name: load;
    animation-duration: 700ms;
}

::-webkit-scrollbar {
    width: 5px;
}

::-webkit-scrollbar-track {
    border-radius: 10px;
    margin-top: 8px;
    margin-bottom: 8px;
}

::-webkit-scrollbar-thumb {
    background: #00000041;
    border-radius: 10px;
}
</style>