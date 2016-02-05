import Ember from 'ember';

export default Ember.Route.extend({
  family: '',
  model: function (params) {
    this.family = params.table_family;
    return this.store.filter('table', { family: params.table_family }, function (table) {
      return table.get('family') === params.table_family;
    });
  },
  setupController: function (controller, model) {
    model.family = this.family;
    controller.set('tables', model);
  }
});
