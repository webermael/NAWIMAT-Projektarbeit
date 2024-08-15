import pygame
import random
from config import Config
from world.world import World
from organisms.population import Population
from organisms.organism import Organism
from evolution.reproduction import reproduction
from utils.visualisation import (render_world, screen_init, screen_update)


class Simulation():
    def __init__(self):
        self.config = Config()
        self.generation_duration = self.config.generation_duration
        self.world = World(self.config)
        self.population = Population(self.config)
        self.screen = screen_init(self.config)
        self.running = False
        self.generation_counter = 0


    def run(self):
        pygame.init()
        while self.generation_duration > 0 and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.running = False
            self.screen.fill((255, 255, 255))

            self.world.spread(self.config)
            self.world.draw(self.config, self.screen)
            self.population.update(self.config, self.world.grid)
            self.population.draw(self.config, self.screen)
            # drawing everything

            screen_update()
            self.generation_duration -= 1
            pygame.time.Clock().tick(self.config.tickspeed)
        pygame.quit()
    

    def normalize_score(self):
        total = 0
        for organism in self.population.organisms: # calculates the total score of all organisms
            if organism.alive:
                organism.score += self.config.survivor_bonus
            organism.score += organism.lifetime
            total += organism.score
        for organism in self.population.organisms:
            organism.score = organism.score / total # divides all scores so they all add up to 1


    def selection(self, organisms):
        start = random.random()
        index = 0
        while start > 0:
            start -= organisms[index].score 
            index += 1
        return organisms[index - 1].nn
    '''
    The selection function picks a random number from 0 to 1, the score of every organism combined is 1 after being normalized by the noramlize score function
    If the start value was 1, you could subtract every score and the last organism in the list, would finall bring it to 0
    This way, any score/score, that is higher than another gets a bigger chance of being selected:
    Imagine one organism having a score of 0.9 (out of 1), so the rest of the organisms would all add up to 0.1
    If the starting value is lower than 0.9, this organism would always be selected, 
    as the other ones could only bring the value down to 0.8 and the strong organism would always get it to 0 or lower
    '''
    

    def new_gen(self):
        new_population = Population(self.config)
        self.normalize_score()

        for organism in range(self.config.population_size):
            new_org = Organism(self.config, 
                               new_population.organisms[organism].position.x, 
                               new_population.organisms[organism].position.y, 
                               reproduction(self.config, self.selection(self.population.organisms), self.selection(self.population.organisms)))
            new_population.organisms[organism] = new_org
        return new_population
    
    def stats(self):
        avg_score = 0
        survival_rate = 0
        for organism in self.population.organisms:
            avg_score += organism.score / self.config.population_size
            if organism.alive:
                survival_rate += (1 / self.config.population_size) * 100
        return round(avg_score, 2), round(survival_rate, 2)


    def reset(self):
        stats = self.stats()
        print("Average Score:", stats[0],f"\nSurvival Rate: {stats[1]}%")
        self.generation_duration = self.config.generation_duration
        self.world = World(self.config)
        self.population = self.new_gen()
        self.screen = screen_init(self.config)

    
    def evolve(self):
        self.running = True
        while self.running:
            self.generation_counter += 1
            print("\nGeneration:", self.generation_counter)
            self.run()
            self.reset()
