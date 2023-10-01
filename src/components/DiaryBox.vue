<template>
    <GlassWindowEffect>
        <h1>Daily Growing History</h1>
        <DiaryRow @onfocus="checkRows" v-model:text="item.text" v-model:emoji="item.emoji"
            v-for="(item, index) in diaryStorge" :key="index" />
    </GlassWindowEffect>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import DiaryRow from './DiaryRow.vue';
import GlassWindowEffect from './GlassWindowEffect.vue';
export default defineComponent({
    data() {
        return {
            diaryStorge: [
                {
                    text: "",
                    emoji: "smile"
                }
            ]
        };
    },
    methods: {
        checkRows() {
            if (this.diaryStorge[this.diaryStorge.length - 1]?.text != "") {
                this.diaryStorge.push({
                    text: ``,
                    emoji: "smile"
                });
            }
            if (this.diaryStorge[this.diaryStorge.length - 1]?.text == "" && this.diaryStorge[this.diaryStorge.length - 2]?.text == "") {
                this.diaryStorge.pop();
            }
            localStorage.setItem("diary", JSON.stringify(this.diaryStorge));
        }
    },
    created() {
        const result: string = localStorage.getItem("diary") ?? '[{"text":"", "emoji":"smile"}]';
        this.diaryStorge = JSON.parse(result);
    },
    components: { DiaryRow, GlassWindowEffect }
});
</script>
<style lang="scss"></style>