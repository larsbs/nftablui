import DS from 'ember-data';

export default DS.Model.extend({
  match: DS.attr('string'),
  action: DS.attr('string'),

  rule: DS.belongsTo('rule', {
    async: true
  })
});
