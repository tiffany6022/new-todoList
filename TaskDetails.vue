<template lang="pug">
#taskdetails
  .ui.transparent.left.icon.input
    input(type="text", placeholder="日期", v-model="item.date", :keyup="$emit('item')")
    i.calendar.alternate.outline.icon
  br
  .ui.transparent.left.icon.input
    input(type="text", placeholder="詳細記事...", v-model="item.content", :keyup="$emit('item')")
    i.pencil.alternate.icon
</template>


<script>
  export default{

    data(){
      return{
      }
    },

    props: ['item']

  }
</script>


<style lang="sass">
  #taskdetails
    padding-left: 2vw
    textarea
      width: 30vw
      height: 10vw
      margin-bottom: 1vw
</style>



