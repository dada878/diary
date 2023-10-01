<template>
    <div class="form-select" :tabindex="tabindex" @blur="open = false">
        <div class="selected" :class="{ open: open }" @click="open = !open">
            {{ selected }}
        </div>
        <div class="items" :class="{ selectHide: !open }">
            <div v-for="(option, i) of options" :key="i" @click="
    selected = option.title;
open = false;
$emit('update:modelValue', option.value);
            ">
                {{ option.title }}
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    props: {
        options: {
            type: Array as () => Array<{title: string, value: string}>,
            required: true,
        },
        default: {
            type: String,
            required: false,
            default: null,
        },
        tabindex: {
            type: Number,
            required: false,
            default: 0,
        },
    },
    data() {
        return {
            selected: this.default
                ? this.default
                : this.options.length > 0
                    ? this.options[0].title
                    : null,
            open: false,
        };
    },
    mounted() {
        this.$emit("input", this.selected);
    },
});
</script>
<style scoped lang="scss">
.form-select {
    position: relative;
    width: 100%;
    text-align: left;
    outline: none;
    height: 47px;
    line-height: 47px;
    margin-left: auto;
    transition: 500ms;
}

.form-select .selected {
    border-radius: 0.3rem;

    // border: 1px solid transparent;
    transition: 200ms;
    background-color: rgba(255, 255, 255, 0.05);
    color: #ffffff;
    opacity: 0.9;
    padding-left: 1em;
    cursor: pointer;
    user-select: none;
    &:hover {
        background-color: rgba(255, 255, 255, 0.10);
    }
}

.form-select .selected.open {
    // border: 1px solid #2c3e50;
    border: none;
}

.form-select .selected:after {
    position: absolute;
    content: "";
    top: 22px;
    right: 1em;
    width: 0;
    height: 0;
    border: 5px solid transparent;
    border-color: #ffffffcc transparent transparent transparent;
}

.form-select .items {
    color: #ffffff;
    overflow: hidden;
    // border-right: 1px solid #2c3e50;
    // border-left: 1px solid #2c3e50;
    // border-bottom: 1px solid #2c3e50;
    position: absolute;
    background-color: rgba(65, 65, 65, 0.536);
    left: 0;
    right: 0;
    z-index: 1;
    opacity: 1;
    pointer-events: all;
    transition: 200ms;

    &:is(.selectHide) {
        pointer-events: none;
        opacity: 0;
    }
}

.form-select .items div {
    color: #ffffff;
    opacity: 0.9;
    padding-left: 1em;
    cursor: pointer;
    user-select: none;
}

.form-select .items div:hover {
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
}
</style>