import DS from 'ember-data';

export default DS.Model.extend({
  handle: DS.attr('number'),
  position: DS.attr('number'),
  expression: DS.attr('string'),
  key: DS.attr('string'),
  statements: DS.attr('statement'),

  chain: DS.belongsTo('chain', {
    async: true
  }),
  //statements: DS.hasMany('statement', {
    //async: true
  //}),
});
