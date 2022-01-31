<template>
    <p class="display-2 text-center font-weight-bold mb-10 mt-16">{{ title }} <span id="explore"></span></p>
</template>

<script>
export default {
    props:["title"]
}
</script>

<style>
#explore{
    background-color: #5C6BC0;
    width: 80px;
    height: 8px;
    margin: 0 auto;
    display: block;
    margin-top: 10px;
}
</style>