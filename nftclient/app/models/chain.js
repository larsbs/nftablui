import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  type: DS.attr('string'),
  hook: DS.attr('string'),
  priority: DS.attr('number'),

  table: DS.belongsTo('table', {
    async: true
  }),
  rules: DS.hasMany('rule', {
    async: true
  })
});
