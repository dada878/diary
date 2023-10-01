<template>
    <GlassWindowEffect>
        <!-- <h1>Add New</h1> -->
        <div class="addnew">
            <FormSelect class="select" :options="[
                {
                    title:'💻 Problem Solving',
                    value:'lol'
                },{
                    title:'⚒️ Project Development', 
                    value:'lol2'
                },{
                    title:'📄 Article Reads', 
                    value:'lol2'
                },{
                    title:'✨ Learning', 
                    value:'lol2'
                }
            ]"></FormSelect>
            <input placeholder="Enter something here..." type="text">
            <button class="btn">Add</button>
        </div>
    </GlassWindowEffect>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import GlassWindowEffect from './GlassWindowEffect.vue';
import FormSelect from './FormSelect.vue';
export default defineComponent({
    data() {
        return {};
    },
    components: { GlassWindowEffect, FormSelect }
});
</script>
<style lang="scss">

.select {
    margin-bottom: 1rem;
}

.addnew {
    display: flex;
    flex-flow: column;
    padding-left: 1rem;
    padding-right: 1rem;
    padding-bottom: 1rem;
    padding-top: 1rem;
}

input {
    background-color: rgba(255, 255, 255, 0.05);
    margin-bottom: 1rem;
    border: none;
    outline: none;
    height: 50px;
    font-size: 16px;
    transition: 200ms;
    color: inherit;
    border-radius: 0.3rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    &::placeholder {
        color: white;
        opacity: 0.5;
    }
    &:hover, &:focus {
        background-color: rgba(255, 255, 255, 0.10);
    }
}

.btn {
    background-color: transparent;
    color: white;
    opacity: 0.9;
    border: white 1px none;
    border-radius: 0.3rem;
    padding: 10px;
    transition: 200ms;
    background-color: rgba(255, 255, 255, 0.15);

    &:hover {
        background-color: rgba(255, 255, 255, 0.25);
        cursor: pointer;
    }
}
</style>