'use strict';

angular.module('superheroSelector', ['ui.bootstrap'])

.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('//');
    $interpolateProvider.endSymbol('//');
})

.controller('selectTypeCtrl', function ($scope, $http) {

})

.controller('selectCharacterCtrl', function ($scope, $http, $modal, $timeout) {

    $timeout(function() {
        $http.post('/ajax/characters', { 'characterType': $scope.characterType })
        .success(function (data) {
            console.log(data);
            $scope.characters = data;
        });
    });

    $scope.preview = function (character) {
        if (!character.taken && character.eligible) {
            var modalInstance = $modal.open({
                templateUrl: '/templates/preview.html',
                controller: 'previewCtrl',
                size: 'lg',
                keyboard: false,
                backdrop: 'static',
                resolve: {
                    character: function () {
                        return character;
                    }
                }
            });
        }
    };
})

.controller('previewCtrl', function ($scope, $modalInstance, $http, character) {

    $scope.character = character;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

})

.controller('secretIdentitiesController', function($scope, $http, $modal) {

    $scope.$watch('participants', function(oldVal, newVal) {
        if (oldVal !== newVal) {
            $scope.setRange(newVal);
        }
    }, true);

    $http.post('/ajax/get-identities')
        .success(function (data) {
            $scope.secretIdentity = data.secretIdentity;
            $scope.participants = data.participants;
        });

    $scope.setRange = function(participants) {
        $scope.participantTrios = [];
        for( var i = 0; i < $scope.participants.length; i = i + 3 ) {
            $scope.participantTrios.push(i);
        }
    };

    $scope.change = function() {
        var modalInstance = $modal.open({
            templateUrl: '/templates/confirm-removal.html',
            controller: 'removeIdentityCtrl',
            size: 'lg',
            keyboard: false,
            backdrop: 'static',
            resolve: {
                characterName: function () {
                    return $scope.secretIdentity.character_name;
                }
            }
        });
    };
})

.controller('removeIdentityCtrl', function ($scope, $modalInstance, characterName) {

    $scope.characterName = characterName;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

});