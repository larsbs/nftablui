module.exports = function(app) {
  var express = require('express');
  var chainsRouter = express.Router();

  var CHAINS = [
    {
      id: 'ip:ip_lars:filter_lars',
      name: 'filter_lars',
      type: 'filter',
      hook: 'input',
      priority: 0,
      table: 'ip:ip_lars',
      rules: [
        'ip:ip_lars:filter_lars:1',
        'ip:ip_lars:filter_lars:2',
        'ip:ip_lars:filter_lars:3',
        'ip:ip_lars:filter_lars:4',
      ]
    }
  ];

  chainsRouter.get('/', function(req, res) {
    res.send({
      'chains': CHAINS
    });
  });

  chainsRouter.post('/', function(req, res) {
    res.status(201);
    var chain = req.body.chain;
    chain.id = chain.table + ':' + chain.name;
    res.send({
      'chain': chain
    });
  });

  chainsRouter.get('/:id', function(req, res) {
    res.send({
      'chain': CHAINS.getById(req.params.id)
    });
  });

  chainsRouter.put('/:id', function(req, res) {
    res.send({
      'chains': {
        id: req.params.id
      }
    });
  });

  chainsRouter.delete('/:id', function(req, res) {
    res.status(204);
    res.send({});
  });

  app.use('/api/chains', chainsRouter);
};
