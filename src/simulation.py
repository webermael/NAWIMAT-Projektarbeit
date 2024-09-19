import pygame
import random
from world.world import World
from organisms.population import Population
from organisms.organism import Organism
from evolution.reproduction import reproduction
from utils.visualisation import screen_init, screen_update

class Simulation():
    '''
    generates world and population
    runs multiple generations
    uses selection based on score to generate new organisms/networks
    '''
    def __init__(self, input_dict):
        self.inputs = input_dict
        self.generation_duration = input_dict["general"]["generation_duration"]
        self.world = World(self.inputs["world"])
        self.population = Population(input_dict["population"], self.inputs["world"]["size"])
        self.screen = screen_init(self.inputs["world"]["size"])
        self.running = False
        self.generation_counter = input_dict["generation_counter"]

    # runs 1 generation for as many steps as set through input
    def run(self):
        while self.generation_duration > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.running = False
            self.screen.fill((255, 255, 255))

            # updates and draws world and population
            self.world.update(self.inputs["world"])
            self.world.draw(self.inputs["world"]["size"]["tile_width"], self.screen)
            self.population.update(self.inputs, self.world.grid)
            self.population.draw(self.inputs["world"]["size"]["tile_width"], self.screen)

            screen_update()
            self.generation_duration -= 1
            # limits the framerate
            pygame.time.Clock().tick(self.inputs["general"]["tickspeed"])

    # adds up all the score bonuses of all organisms
    def score_calculation(self):
        for organism in self.population.organisms:
            if organism.alive:
                organism.score += self.inputs["population"]["interactions"]["survivor_bonus"]
            organism.score += organism.lifetime

    # normalizes score for selection
    def normalize_score(self):
        total = 0
        for organism in self.population.organisms: # calculates the total score of all organisms
            total += organism.score
        if total != 0:
            for organism in self.population.organisms:
                organism.score = organism.score / total # divides all scores so they all add up to 1

    # selects organisms fit for reproduction, a higher score gets a better chance to be selected
    def selection(self, organisms):
        start = random.random()
        index = 0
        while start > 0:
            start -= organisms[index].score 
            index += 1
        return organisms[index - 1].nn

    # creates a fresh population for the next generation
    def new_gen(self):
        # uses coords_only in population as the organism objects would be replaced anyway
        new_population = Population(self.inputs["population"], self.inputs["world"]["size"], True)
        self.normalize_score()
        # creates new organisms whose networks are combined from successful organisms from the previous generation
        for organism in range(self.inputs["population"]["population_size"]):
            new_org = Organism(self.inputs["population"]["organisms"], 
                               new_population.organism_coords[organism][0], 
                               new_population.organism_coords[organism][1], 
                               reproduction(self.inputs["population"], self.selection(self.population.organisms), self.selection(self.population.organisms)))
            new_population.organisms.append(new_org)
        return new_population

    # calculates some statistics from the current generation
    def stats(self):
        avg_score = 0
        survival_rate = 0
        for organism in self.population.organisms:
            avg_score += organism.score / len(self.population.organisms)
            if organism.alive:
                survival_rate += (1 / len(self.population.organisms)) * 100
        print(f"Average Score: {round(avg_score, 2)}", f"\nSurvival Rate: {round(survival_rate, 2)}%")

    # resets all variables necessary for a new generation and prints stats
    def reset(self):
        self.score_calculation()
        self.stats()
        self.generation_duration = self.inputs["general"]["generation_duration"]
        if self.running:
            self.world = World(self.inputs["world"])
            self.population = self.new_gen()

    # runs the whole simulation with multiple generations
    def evolve(self):
        pygame.init()
        self.running = True
        while self.running:
            self.generation_counter += 1
            print("\nGeneration:", self.generation_counter)
            pygame.display.set_caption(f"Evolvator Generation: {self.generation_counter}")
            self.run()
            self.reset()
        pygame.quit()
