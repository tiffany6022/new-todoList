<template lang="pug">
#app
  .ui.action.input
    input(type="text", v-model="todo")
    button.ui.icon.button(@click="addTask()")
      i.plus.icon

  .ui.checkbox(v-for="task in tasks")
    input(type="checkbox", :id="task.title", @click="", v-model="task.done")
    label(:for="task.title", v-if="task.done")
      del {{ task.title }}
    label(:for="task.title", v-else) {{ task.title }}
    i.close.icon(@click.stop="deleteTask(task)", v-if="task.done")
</template>


<script>
  export default{
    data(){
      return{
        todo: "abc",
        tasks: []
      }
    },
    methods: {
      addTask: function(){
        var tsk = this.todo;
        if(tsk){
          this.tasks.push({
            title: tsk,
            done: false
          });
          this.todo = "";
        }
      },
      deleteTask: function(tsk){
        this.tasks.splice(this.tasks.indexOf(tsk), 1);
      },
    },
  }
</script>


<style lang="sass">

</style>
